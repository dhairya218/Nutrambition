from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from nutra.models import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from .forms import Feedbackform

# Create your views here.


@login_required(login_url='login')
def home(request):
    return render(request, "home.html")


@csrf_exempt
def signin(request):
    if request.user.is_authenticated:
        print("u r signeddddddddddddd")
        return redirect("home")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(
                request, "login.html",
                messages.error(request, "username or password is undefine!")
            )

    return render(request, "login.html")


@csrf_exempt
def signup(request):
    if request.user.is_authenticated:
        print("u r authenticated signuppp")
        return redirect("home")

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request, "signup.html", messages.error(request, "Username already exists. Please choose another!"))
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, "signup.html", messages.error(request, "Username already exists. Please choose another!"))
                else:
                    request.session['username'] = username
                    request.session['email'] = email
                    request.session['firstname'] = firstname
                    request.session['lastname'] = lastname
                    request.session['password'] = password
                    return redirect("userdetail")
        else:
            return render(request, "signup.html", messages.error(request, "Passwords does not match!"))
    return render(request, "signup.html")


@csrf_exempt
def userdetail(request):
    if request.user.is_authenticated:
        print("u r signeddddddddddddd via userdetail")
        return redirect("home")
    if request.method == "POST":

        # get user details from session
        username = request.session.get('username')
        email = request.session.get('email')
        firstname = request.session.get('firstname')
        lastname = request.session.get('lastname')
        password = request.session.get('password')

        # get user personal information
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        city = request.POST.get('city')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        t_weight = request.POST.get('t_weight')
        medical_condition = request.POST.get('medical_condition')

        user = User.objects.create_user(
            username=username, email=email, first_name=firstname, last_name=lastname, password=password)
        user.save()
        print(user.pk)
        user_info = UserDetails(
            user_acc=user,
            gender=gender,
            age=age,
            user_height=height,
            user_weight=weight,
            target_weight=t_weight,
            medical_condition=medical_condition,
            emotional_health='Excessive Stress',
            city=city
        )
        user_info.save()

        return redirect("home")
    return render(request, "userdetail.html")


def logout_request(request):
    print("You have been logged out111111111111")
    logout(request)
    print("You have been logged out2222")
    return redirect("login")


def about(request):
    return render(request, "about-us.html")


@csrf_exempt
def contact(request):
    if request.method == "POST":

        name = request.POST["name"]
        email = request.POST["email"]
        mob_no = request.POST["mob_no"]
        comment = request.POST["comment"]

        admin_email = 'aaditya.rola110711@marwadiuniversity.ac.in'
        msg = f'''Dear {name},
        Thank you for your interest in Nutrabition Solutions Ltd. We appreciate your inquiry. One of our representatives will contact you shortly.'''
        sub = "Thank you for your Inquiry | Team Nutrabmition Solutions Ltd."

        send_mail_data = MIMEMultipart()
        send_mail_data['From'] = admin_email
        send_mail_data['To'] = email
        send_mail_data['Subject'] = sub

        # Attach the message
        send_mail_data.attach(MIMEText(msg, 'plain'))

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(admin_email, 'iocu lnlr mceu nwou')
            server.sendmail(admin_email, email,  send_mail_data.as_string())
            server.quit()
        except Exception as e:
            print("SMTP Error:", e)

    return render(request, "contact.html")

def classes(request):
    return render(request, "class-details.html")

def services(request):
    return render(request, "services.html")

def class_timetable(request):
    return render(request, "class-timetable.html")

def calculator(request):
    return render(request, "calculators.html")

def bmi(request):
    return render(request, "bmi.html")

def bmr(request):
    return render(request, "bmr.html")

def calorie(request):
    return render(request, "calorie.html")

def excercise(request):
    return render(request, "excercise.html")

def favoviretes(request):
    return render(request, "favorites.html")

def team(request):
    return render(request, "team.html")

def gallery(request):
    return render(request, "gallery.html")

def blog(request):
    return render(request, "blog.html")

def blogdetails(request):
    return render(request, "blog-details.html")

def excercise_deatil(request,param=None):
    print(param)
    return render(request, "exercise-details.html")

def explore1(request):
    return render(request, "explore1.html")

def explore2(request):
    return render(request, "explore2.html")

def feedback(request):
    form = Feedbackform()
    if request.method == "POST":
        form = Feedbackform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Feedbackform()
    return render(request, "feedback.html", {"form": form})

def feedback_success_view(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'feedback_success.html', {'feedbacks': feedbacks})

def booking(request):
    return render(request, "booking.html")