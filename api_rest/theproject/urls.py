from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ProjectList, ProjectDetail,  ProjectHighlight

urlpatterns = [
    path('projects/', ProjectList.as_view()),
    path('projects/<int:pk>/', ProjectDetail.as_view()),
    path('projects/<int:pk>/highlight/', ProjectHighlight.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)