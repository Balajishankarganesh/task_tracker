from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer
from django.db.models import Count
from datetime import date

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    @action(detail=True, methods=['get'])
    def summary(self, request, pk=None):
        project = self.get_object()
        total_tasks = project.tasks.count()
        completed_tasks = project.tasks.filter(status='done').count()
        pending_tasks = project.tasks.exclude(status='done').count()
        return Response({
            'total': total_tasks,
            'completed': completed_tasks,
            'pending': pending_tasks
        })

    @action(detail=True, methods=['get'])
    def dashboard(self, request, pk=None):
        project = self.get_object()
        status_counts = project.tasks.values('status').annotate(count=Count('status'))
        overdue_tasks = project.tasks.filter(due_date__lt=date.today(), status__in=['todo','inprogress','review']).count()
        upcoming_tasks = project.tasks.filter(due_date__gte=date.today()).order_by('due_date')[:3]
        upcoming_tasks_data = TaskSerializer(upcoming_tasks, many=True).data
        return Response({
            'total_tasks': project.tasks.count(),
            'status_counts': list(status_counts),
            'overdue_tasks': overdue_tasks,
            'upcoming_tasks': upcoming_tasks_data,
        })

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        project_name = self.request.query_params.get('project')
        status = self.request.query_params.get('status')
        if project_name:
            queryset = queryset.filter(project__name=project_name)
        if status:
            queryset = queryset.filter(status=status)
        return queryset
