from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    '''
    author      글쓴이
    subject	    질문의 제목
    content 	질문의 내용
    create_date	질문을 작성한 일시
    modify_date 질문을 수정한 일시
    voter       추천
    '''
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author_question', null=True)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')

    def __str__(self):
        return self.subject


class Answer(models.Model):
    '''
    author      글쓴이
    question    질문 (어떤 질문의 답변인지 알아야하므로 질문 속성이 필요하다.)
    content     답변의 내용
    create_date	답변을 작성한 일시
    modify_date 답변을 수정한 일시
    voter       추천
    '''
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author_answer', null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')


class Comment(models.Model):
    '''
    author	    댓글 작성자
    content	    댓글 내용
    create_date	댓글 작성일시
    modify_date	댓글 수정일시
    question	댓글의 질문
    answer	    댓글의 답변
    '''
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(
        Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(
        Answer, null=True, blank=True, on_delete=models.CASCADE)
