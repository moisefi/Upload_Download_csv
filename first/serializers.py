from dataclasses import fields
from rest_framework import serializers

from .models import FileModel


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileModel
        fields = "__all__"


class MultipleFileSerializer(serializers.Serializer):
    files = serializers.ListField(
        child=serializers.FileField()
    )



