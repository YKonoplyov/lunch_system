from rest_framework.permissions import BasePermission

from vote_service.serivces import has_user_voted


class HasNotVoted(BasePermission):
    message = "You`ve already voted today"
    def has_permission(self, request, view):
        return has_user_voted(request)