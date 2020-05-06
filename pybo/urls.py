from django.urls import path

from . import views


app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    # http://locahost:8000/pybo/answer/create/2/ 와 같은 페이지를 요청하면 views.answer_create 함수를 호출
    path('answer/create/<int:question_id>/',
         views.answer_create, name='answer_create'),
]
