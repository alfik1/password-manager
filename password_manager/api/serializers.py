from rest_framework import serializers
from rest_framework.validators  import ValidationError
from rest_framework.response import Response
from api.models import Password




class PasswordSerializer(serializers.ModelSerializer):
    
    user=serializers.CharField(read_only=True)
    password=serializers.CharField(write_only=True)
    
    class Meta:
        model=Password
        fields=["user","description","password","email"]

    # def validate(self,attrs):

    #     email_exists = UserModel.objects.filter(email=attrs["email"]).exists()

    #     if email_exists:
    #         raise ValidationError("Email has already been used")
    #     return super().validate(attrs)

    def create(self, validated_data):
        return Password.objects.create_user(**validated_data)