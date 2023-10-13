from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from teachers.models import Teacher

from .serializers import StudentSerializar
from .models import Student


class StudentList(APIView):
    def post(self, request, teacher_pk):
        teacher = get_object_or_404(Teacher, pk=teacher_pk)
        serializer = StudentSerializar(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(teacher=teacher)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TeacherStudentList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        students = request.user.students.all()
        serializer = StudentSerializar(students, many=True)
        return Response(serializer.data)
