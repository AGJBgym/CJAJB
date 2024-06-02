from cjajb import models
from cjajb.serializers import TeamSerializer, UserSerializer, AthleteSerializer
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render
from knox.views import LoginView as KnoxLoginView
from rest_framework import permissions, viewsets
from rest_framework.authtoken.serializers import AuthTokenSerializer

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
    
class AthleteViewSet(viewsets.ModelViewSet):
    queryset = models.athlete.Athlete.objects.all()
    serializer_class = AthleteSerializer
