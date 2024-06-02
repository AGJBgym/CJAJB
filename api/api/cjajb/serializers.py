from cjajb.models.athlete import Athlete
from cjajb.models.team import Team
from cjajb.models.championship import Championship
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "url",
            "username",
            "email",
            "first_name",
            "last_name",
            "teams"
        ]
        
class TeamSerializer(serializers.HyperlinkedModelSerializer):
    athletes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='athlete-detail')
    class Meta:
        model = Team
        fields = '__all__'
        
class AthleteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Athlete
        fields = '__all__'
        
class ChampionshipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Championship
        fields = '__all__'