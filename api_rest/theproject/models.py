from django.db import models
from django.conf import settings

ROLES = [
    ('AUTHOR', 'AUTHOR'),
    ('CONTRIBUTOR', 'CONTRIBUTOR'),
]

TYPES = [
    ('BACKEND', 'BACKEND'),
    ('FRONTEND', 'FRONTEND'),
    ('IOS', 'IOS'),
    ('ANDROID', 'ANDROID')
]

TAGS = [
    ('BUG', 'BUG'),
    ('TASK', 'TASK'),
    ('UPGRADE', 'UPGRADE')
]

PRIORITIES = [
    ('LOW', 'LOW'),
    ('MEDIUM', 'MEDIUM'),
    ('HIGH', 'HIGH')
]

STATUS = [
    ('TODO', 'TODO'),
    ('IN PROGRESS', 'IN PROGRESS'),
    ('DONE', 'DONE')
]


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    type = models.CharField(choices=TYPES, max_length=8)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author')


class Contributor(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, related_name='contributors')
    role = models.CharField(max_length=11, choices=ROLES, default='CONTRIBUTOR')


class Issue(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=2048)
    tags = models.CharField(choices=TAGS, max_length=7)
    priority = models.CharField(choices=PRIORITIES, max_length=6, default='LOW')
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, max_length=11, default='TODO')
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='project', on_delete=models.CASCADE)
    assignee = models.ForeignKey(to=Contributor, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    description = models.TextField(max_length=2048)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    issue = models.ForeignKey(to=Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

