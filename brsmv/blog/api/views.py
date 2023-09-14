from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import BlogSerializer
from ..models import Blog


class BlogView(APIView):
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        try:
            if id:
                username = self.request.user
                blog = Blog.objects.filter(id=id, user__username=username)
                serializer = BlogSerializer(blog, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                username = self.request.user
                blog = Blog.objects.filter(user__username=username)
                serializer = BlogSerializer(blog, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": e})

    def post(self, request):
        try:
            serializer = BlogSerializer(data=request.data)
            request.data['user'] = self.request.user.id
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': e}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None):
        try:
            blog = get_object_or_404(Blog, id=id)
            if blog:
                serializer = BlogSerializer(blog, partial=True, data=request.data)
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
            blog = get_object_or_404(Blog, id=id)
            if blog:
                blog.delete()
                return Response({'message': 'Data has been deleted successfully'}, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({'message': 'Id not found'}, status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist as e:
            return Response({'message': 'Id not found'}, status.HTTP_400_BAD_REQUEST)
