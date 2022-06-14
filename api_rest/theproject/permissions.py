from rest_framework import permissions
from django.core.exceptions import ObjectDoesNotExist
from .models import Contributor, Project


class IsAuthorContributorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        try:
            contributor = Contributor.objects.get(user=request.user)
            id = request.parser_context['kwargs']['pk']
            lst = Contributor.objects.filter(project__id=id)
            for i in lst:
                if request.method in permissions.SAFE_METHODS and i.id == contributor.id:
                    return True
        except ObjectDoesNotExist:
            pass

        if request.method and obj.author == request.user in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.author == request.user
