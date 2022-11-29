from django.shortcuts import render
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from api.serializers import PasswordSerializer
from api.models import Password
from rest_framework import permissions,authentication
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET',])
def ApiOverview(request):
    api_urls = {
        'token':'token/',
        'all passwords': '/',
        'Search by description': '/?description=description_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }
  
    return Response(api_urls)

class PasswordView(ModelViewSet):
    serializer_class = PasswordSerializer
    queryset=Password.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def create(self,request,*args,**kwargs):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            response={
                "message":"User has successfully signed up","data":serializer.data
            }
            return Response(data=response ,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        
    def get_queryset(self):

        return Password.objects.filter(user=self.request.user)

#To create a password
@api_view(['POST'])
def add_password(request):
    print(request.data)
    pwd = PasswordSerializer(data=request.data)
    print(request.data)
    
    # validating for already existing data
    if Password.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
    print(request.data)
    if pwd.is_valid():
        pwd.save()
        return Response(pwd.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def view_passwords(request):
    
    # checking for the parameters from the URL
    if request.query_params:
        pwd = Password.objects.filter(**request.query_param.dict())
    else:
        pwd = Password.objects.all()
  
    # if there is something in Password else raise error
    if pwd:
        data = PasswordSerializer(pwd)
        return Response(data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_pasword(request, pk):
	pwd = Password.objects.get(pk=pk)
	data = PasswordSerializer(instance=pwd, data=request.data)

	if data.is_valid():
		data.save()
		return Response(data.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_password(request, pk):
    pwd = get_object_or_404(pwd, pk=pk)
    pwd.delete()
    return Response(status=status.HTTP_202_ACCEPTED)