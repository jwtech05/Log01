from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from .models import member
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def login_view(request): #로그인 뷰

        if request.method == "POST": #POST메소드를 이용해서 요청할 것이다
                username = request.POST["username"] #POST로 요청받는 username
                password = request.POST["password"] #POST로 요청받는 password
                user = authenticate(username=username, password=password) #POST로 요청받은 것이 기존에 있는 username과 password와 맞는지 확인
                if user is not None: #인증성공시 콘솔 출력 화면
                        print("인증성공")
                        login(request, user)
                else: #인증실패시 콘솔 출력 화면
                        print("인증실패")

        return render(request, 'login/log.html') #html로 연결되어 화면을 랜더링(그리기) 한다.

def logout_view(request): #로그아웃 뷰
        logout(request)
        return redirect("logins:login") #로그아웃시 로그인 페이지로 돌아간다

def signup_view(request): #회원가입 뷰
        if request.method =="POST": #POST메소드를 이용해서 요청할 것이다
                profile_img = request.FILES["profile_img"]
                username = request.POST["username"] #POST로 요청받는 username
                password = request.POST["password"] #POST로 요청받는 password
                firstname = request.POST["firstname"] #POST로 요청받는 name
                lastname = request.POST["lastname"]
                email = request.POST["email"] #POST로 요청받는 email
                dept = request.POST["dept"] #POST로 요청받는 dept
                add = request.POST["add"]

                user = member.objects.create_user(username, email, password) #member 데이터베이스와 연결해서 데이터 베이스에 정보 등록
                user.dept = dept #부서 항목 추가
                user.first_name = firstname
                user.last_name = lastname
                user.profile_img = profile_img
                user.add = add
                user.save() #저장
                return redirect("logins:login") #회원가입 후 로그인 화면으로 돌아간다

        return render(request, "login/signup.html") #html로 연결되어 화면을 랜더링(그리기) 한다.

