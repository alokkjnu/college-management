from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status, viewsets

from ..api.serializers import RegistrationSerializer


@api_view(['POST', ])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        message = "User has been logged out."
        return Response({"message": message}, status=status.HTTP_200_OK)


# class RegistrationView(viewsets.ViewSet):
#     serializer_class = RegistrationSerializer
#
#     def create(self, request):
#         try:
#             if request.method == 'POST':
#                 serializer = RegistrationSerializer(data=request.data)
#                 data = {}
#                 if serializer.is_valid():
#                     account = serializer.save()
#                     data['response'] = "User Registered Successfully"
#                     data['username'] = account.email
#                     data['mobile_no'] = account.mobile_no
#                     data['email'] = account.email
#                     data['first_name'] = account.first_name
#                     data['middle_name'] = account.middle_name
#                     data['last_name'] = account.last_name
#
#                     token = Token.objects.get(user=account).key
#                     data['token'] = token
#                     # success_msg = ""
#                     # return Response(serializer.data, status=status.HTTP_201_CREATED)
#                 else:
#                     data = serializer.errors
#                 return Response({"data": data}, status=status.HTTP_201_CREATED)
#
#         except Exception as e:
#             return Response({"message": e})

@api_view(['POST', ])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
#
            data['response'] = "User Registered Successfully"
            data['username'] = account.email
            data['mobile_no'] = account.mobile_no
            data['email'] = account.email
            data['first_name'] = account.first_name
            data['middle_name'] = account.middle_name
            data['last_name'] = account.last_name

            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response({"data": data}, status=status.HTTP_201_CREATED)
