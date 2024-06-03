from cjajb.models.athlete import Athlete
from cjajb.models.category import Category
from cjajb.models.championship import Championship
from cjajb.models.competition import Competition
from cjajb.models.discipline import Discipline
from cjajb.models.meeting import Meeting
from cjajb.models.scale import Scale
from cjajb.models.team import Team
from cjajb.models.venue import Venue
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "url", "username", "email", "first_name", "last_name", "teams"]


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    athletes = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="athlete-detail"
    )

    class Meta:
        model = Team
        fields = "__all__"


class AthleteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Athlete
        fields = "__all__"


class ChampionshipSerializer(serializers.HyperlinkedModelSerializer):
    meetings = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="meeting-detail"
    )

    class Meta:
        model = Championship
        fields = "__all__"


class VenueSerializer(serializers.HyperlinkedModelSerializer):
    meetings = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="meeting-detail"
    )

    class Meta:
        model = Venue
        fields = "__all__"


class MeetingSerializer(serializers.HyperlinkedModelSerializer):
    competitions = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="competition-detail"
    )

    class Meta:
        model = Meeting
        fields = "__all__"


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    athletes = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="athlete-detail"
    )
    competitions = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="competition-detail"
    )

    class Meta:
        model = Category
        fields = "__all__"


class ScaleSerializer(serializers.HyperlinkedModelSerializer):
    competitions = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="competition-detail"
    )

    class Meta:
        model = Scale
        fields = "__all__"


class CompetitionSerializer(serializers.HyperlinkedModelSerializer):
    competitions = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="competition-detail"
    )

    class Meta:
        model = Competition
        fields = "__all__"


class DisciplineSerializer(serializers.HyperlinkedModelSerializer):
    competitions = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="competition-detail"
    )

    class Meta:
        model = Discipline
        fields = "__all__"
