from rest_framework import serializers

from cartApp.models import UsersCart


class UsersCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersCart
        fields ='__all__'