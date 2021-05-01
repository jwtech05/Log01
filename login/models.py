from django.db import models
from django.contrib.auth.models import AbstractUser

class member(AbstractUser): #AbstractUser를 통해 데이터 클래스 생성
    dept = models.CharField(max_length=30) #기존있는 항목에 부서 항목 추가

    class Meta:
        db_table = "Accounts" #데이터베이스에 저장되는 테이블 이름 설정
