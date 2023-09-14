from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import CollegeSerializer
from ..models import College


class CollegeView(APIView):
    serializer_class = CollegeSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        try:
            if id:
                college = College.objects.filter(id=id)
                serializer = CollegeSerializer(college, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                college = College.objects.filter()
                serializer = CollegeSerializer(college, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": e})

    def post(self, request):
        try:
            try:
                id = College.objects.filter().last().id
            except AttributeError as e:
                id = 0
            serializer = CollegeSerializer(data=request.data)
            request.data['id'] = id + 1
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': e}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None):
        try:
            subject = get_object_or_404(College, id=id)
            if subject:
                serializer = CollegeSerializer(subject, partial=True, data=request.data)
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
            subject = get_object_or_404(College, id=id)
            if subject:
                subject.delete()
                return Response({'message': 'Data has been deleted successfully'}, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({'message': 'Id not found'}, status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist as e:
            return Response({'message': 'Id not found'}, status.HTTP_400_BAD_REQUEST)
