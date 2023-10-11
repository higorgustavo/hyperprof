from rest_framework.permissions import BasePermission


class TeacherListPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method not in ("PUT", "DELETE"):
            return True
        return request.user and request.user.is_authenticated

        # ou
        # return bool(
        #         request.method not in ("PUT", "DELETE")
        #         or request.user
        #         and request.user.is_authenticated
        #     )
