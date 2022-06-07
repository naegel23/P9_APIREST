from rest_framework import viewsets, permissions
from .permissions import IsAuthorOrReadOnly
from .models import Project, Contributor, Issue, Comment
from .serializers import ProjectSerializer, ContributorSerializer, IssueSerializer, CommentSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]
    queryset = Project.objects.all()
    filterset_fields = ['author', 'type']
    search_fields = ['title', 'type']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ContributorViewSet(viewsets.ModelViewSet):
    serializer_class = ContributorSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Contributor.objects.all()
    filterset_fields = ['role', 'project']


class IssueViewSet(viewsets.ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]
    queryset = Issue.objects.all()
    filterset_fields = ['project', 'assignee', 'priority', 'author', 'status']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]
    queryset = Comment.objects.all()
    filterset_fields = ['issue']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
