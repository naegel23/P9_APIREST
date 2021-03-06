from django.urls import path, include
from .views import ProjectViewSet, ContributorViewSet, IssueViewSet, CommentViewSet


from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'contributors', ContributorViewSet)
router.register(r'issues', IssueViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
