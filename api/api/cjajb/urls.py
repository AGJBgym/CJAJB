from cjajb import views
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("users", views.UserViewSet)
router.register("teams", views.TeamViewSet)
router.register("athletes", views.AthleteViewSet)
router.register("championships", views.ChampionshipViewSet)
router.register("venues", views.VenueViewSet)
router.register("meetings", views.MeetingViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
