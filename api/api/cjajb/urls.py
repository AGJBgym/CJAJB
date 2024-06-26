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
router.register("categories", views.CategoryViewSet)
router.register("competitions", views.CompetitionViewSet)
router.register("disciplines", views.DisciplineViewSet)
router.register("scales", views.ScaleViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
