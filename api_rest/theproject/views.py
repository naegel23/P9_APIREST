from rest_framework import viewsets, permissions
from .permissions import IsAuthorContributorOrReadOnly
from .models import Project, Contributor, Issue, Comment
from .serializers import ProjectSerializer, ContributorSerializer, IssueSerializer, CommentSerializer



class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorContributorOrReadOnly]
    queryset = Project.objects.all()
    # Project.objects.filter(contributor__user=request.user)
    filterset_fields = ['author', 'type']
    search_fields = ['title', 'type']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
    def get_queryset(self):
        return (Project.objects.filter(contributors__user=self.request.user) | Project.objects.filter(
            author=self.request.user)).distinct()


class ContributorViewSet(viewsets.ModelViewSet):
    serializer_class = ContributorSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Contributor.objects.all()
    filterset_fields = ['role', 'project']


class IssueViewSet(viewsets.ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorContributorOrReadOnly]
    queryset = Issue.objects.all()
    filterset_fields = ['project', 'assignee', 'priority', 'author', 'status']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorContributorOrReadOnly]
    queryset = Comment.objects.all()
    filterset_fields = ['issue']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

