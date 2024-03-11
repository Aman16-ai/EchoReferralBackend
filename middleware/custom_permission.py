from rest_framework import permissions

class IsAdminOrOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj == request.user 
    
class IsAdminOrUserProfileOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or request.method == 'GET':
            return True
        return obj.userProfile.user == request.user

class IsAdminOrReferralRequestOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or request.method == 'GET':
            return True
        return obj.candidate.user == request.user