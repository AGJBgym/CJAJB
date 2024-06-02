from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('users', views.UserViewSet)
router.register('teams', views.TeamViewSet)
router.register('athletes', views.AthleteViewSet)
router.register('championships', views.ChampionshipViewSet)

urlpatterns = [
    path('', include(router.urls)),
]