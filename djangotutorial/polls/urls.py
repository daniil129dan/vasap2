from django.urls import path, include
from .views import UserListView, QuestionViewSet, ChoiceViewSet, UserViewSet
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'choices', ChoiceViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
    path("data", UserListView.as_view(), name="user_list"),
    path('', include(router.urls)),
]