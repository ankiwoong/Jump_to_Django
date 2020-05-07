from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    '''
    author      글쓴이
    subject	    질문의 제목
    content 	질문의 내용
    create_date	질문을 작성한 일시
    '''
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject


class Answer(models.Model):
    '''
    author      글쓴이
    question    질문 (어떤 질문의 답변인지 알아야하므로 질문 속성이 필요하다.)
    content     답변의 내용
    create_date	답변을 작성한 일시
    '''
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
