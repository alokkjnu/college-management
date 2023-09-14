from rest_framework import serializers
from ..models import College


class CollegeSerializer(serializers.Serializer):
    college = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = College
        fields = '__all__'
