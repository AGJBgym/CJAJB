from django.shortcuts import render
from django.contrib.auth.models import User

from knox.views import LoginView as KnoxLoginView
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login
from rest_framework import viewsets
from cjajb import models
from cjajb.serializers import TeamSerializer, UserSerializer

# Create your views here.

class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class TeamViewSet(viewsets.ModelViewSet):
    queryset = models.team.Team.objects.all()
    serializer_class = TeamSerializer
