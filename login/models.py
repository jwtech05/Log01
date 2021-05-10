from django.db import models
from django.contrib.auth.models import AbstractUser


class member(AbstractUser): #AbstractUser를 통해 데이터 클래스 생성

    DEPT_CHOICES = {
        ('mju', 'MJU'),
        ('uplex', 'UPLEX'),
        ('not-specified', 'Not Specified')
    }
    password2 = models.CharField
    dept = models.CharField(max_length=100, choices=DEPT_CHOICES, null=True) #기존있는 항목에 부서 항목 추가
    profile_img = models.ImageField(null=True)
    add = models.CharField(max_length=100, null=True, default='settings.MEDIA_ROOT/media/MJUPLEX1.png')

    class Meta:
        db_table = "Accounts" #데이터베이스에 저장되는 테이블 이름 설정
