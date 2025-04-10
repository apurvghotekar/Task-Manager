from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'priority', 'due_date']

    def get_queryset(self):
        # Return only the tasks for the authenticated user
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Set the task's user to the currently authenticated user
        serializer.save(user=self.request.user)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Ensure users can only access their own tasks
        return Task.objects.filter(user=self.request.user)
