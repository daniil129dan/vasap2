from django.views.generic import TemplateView
from django.http import HttpResponse
from .nocodeb_api import get_users
from rest_framework import viewsets
from .models import Question, Choice, User
from .serializers import QuestionSerializer, ChoiceSerializer, UserSerializer


class UserListView(TemplateView):
    template_name = 'app/template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        table_id = 'm3z6v1b977wlhfm'  # ID вашей таблицы
        try:
            records = get_users(table_id)
            print(records)
        except Exception as e:
            records = []
            print(e)
        
        context['records'] = records
        return context


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Create your views here.
