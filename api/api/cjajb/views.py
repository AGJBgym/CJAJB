from cjajb import models, serializers
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
        user = serializer.validated_data["user"]
        login(request, user)
        return super(LoginView, self).post(request, format=None)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = models.team.Team.objects.all()
    serializer_class = serializers.TeamSerializer


class AthleteViewSet(viewsets.ModelViewSet):
    queryset = models.athlete.Athlete.objects.all()
    serializer_class = serializers.AthleteSerializer


class ChampionshipViewSet(viewsets.ModelViewSet):
    queryset = models.championship.Championship.objects.all()
    serializer_class = serializers.ChampionshipSerializer


class VenueViewSet(viewsets.ModelViewSet):
    queryset = models.venue.Venue.objects.all()
    serializer_class = serializers.VenueSerializer


class MeetingViewSet(viewsets.ModelViewSet):
    queryset = models.meeting.Meeting.objects.all()
    serializer_class = serializers.MeetingSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.category.Category.objects.all()
    serializer_class = serializers.CategorySerializer