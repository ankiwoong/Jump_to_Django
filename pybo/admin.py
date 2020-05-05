from django.contrib import admin

from .models import Question


# Question 모델을 관리자에 등록
# 관리자 화면에서 제목으로 질문을 검색할 수 있는 기능을 추가
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Question, QuestionAdmin)
