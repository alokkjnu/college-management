from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import CourseSerializer, SubjectSerializer
from ..models import Course, Subject


class CourseView(APIView):
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        try:
            if id:
                course = Course.objects.filter()
                serializer = CourseSerializer(course, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                course = Course.objects.filter()
                serializer = CourseSerializer(course, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": e})

    def post(self, request):
        try:
            try:
                id= Course.objects.filter().last().id
            except AttributeError as e:
                id = 0
            serializer = CourseSerializer(data=request.data)
            request.data['id'] = id+1
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': e}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None):
        try:
            course = get_object_or_404(Course, id=id)
            if course:
                serializer = CourseSerializer(course, partial=True, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': 'Id not found'}, status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist as e:
            return Response({'message': 'Id not found'}, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        try:
            course = get_object_or_404(Course, id=id)
            if course:
                course.delete()
                return Response({'message': 'Data has been deleted successfully'}, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({'message': 'Id not found'}, status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist as e:
            return Response({'message': 'Id not found'}, status.HTTP_400_BAD_REQUEST)


class SubjectView(APIView):
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        try:
            if id:
                subject = Subject.objects.filter(id=id)
                serializer = CourseSerializer(subject, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                subject = Subject.objects.filter()
                serializer = SubjectSerializer(subject, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": e})

    def post(self, request):
        try:
            try:
                id = Subject.objects.filter().last().id
            except AttributeError as e:
                id = 0
            serializer = SubjectSerializer(data=request.data)
            request.data['id'] = id+1
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': e}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None):
        try:
            subject = get_object_or_404(Subject, id=id)
            if subject:
                serializer = SubjectSerializer(subject, partial=True, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': 'Id not found'}, status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist as e:
            return Response({'message': 'Id not found'}, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        try:
            subject = get_object_or_404(Subject, id=id)
            if subject:
                subject.delete()
                return Response({'message': 'Data has been deleted successfully'}, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({'message': 'Id not found'}, status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist as e:
            return Response({'message': 'Id not found'}, status.HTTP_400_BAD_REQUEST)
