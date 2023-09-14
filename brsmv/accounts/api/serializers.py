# from django.contrib.auth.models import User
from rest_framework import serializers
from ..models import User


class RegistrationSerializer(serializers.ModelSerializer):
    # account = serializers.StringRelatedField(read_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'middle_name', 'last_name', 'mobile_no', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'error': 'password and confirm password should be same!'})
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'Email already exists!'})
        if User.objects.filter(mobile_no=self.validated_data['mobile_no']).exists():
            raise serializers.ValidationError({'error': 'Mobile Number already exists!'})

        account = User(username=self.validated_data['email'] ,email=self.validated_data['email'], mobile_no=self.validated_data['mobile_no'],
                       first_name=self.data['first_name'], middle_name=self.data['middle_name'],
                       last_name=self.data['last_name'])
        account.set_password(password)
        account.save()

        return account
