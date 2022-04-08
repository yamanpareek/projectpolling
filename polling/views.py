from random import randint

from django.core.mail import send_mail
from django.shortcuts import render
from django.db import connection


# Create your views here.
def firstpage(request):
    return render(request, "index.html")


def loginpage(request):
    return render(request, "loginpage.html")


def signuppage(request):
    return render(request, "signuppage.html")


def page(request):
    FullName = request.GET['name']
    Age = request.GET['ag']
    Email = request.GET['email']
    PhoneNumber = request.GET['pnum']
    Password = request.GET['psw']
    Gender = request.GET['gender']

    cursor = connection.cursor()
    query= "select * from users where email = '"+Email+"'"
    cursor.execute(query)
    data = cursor.fetchall()

    if len(data)>0:
        return render(request,"loginpage.html")

    else:
        otp = randint(100000, 999999)
        strotp = str(otp)
        query = "insert into users (fullname , age , email , phonenumber , password , gender, OTP ) values (%s, %s , %s, %s , %s , %s , %s)"
        value = (FullName, Age, Email, PhoneNumber, Password, Gender, strotp)
        cursor.execute(query, value)
        body = 'your otp for our portal you signedup with email ' + Email + ' is ' + strotp
        send_mail('OTP for Verification', body, 'kunalgautam.ee21@jecrc.ac.in', [Email])
        data = {"email": Email}
        return render(request, "verifyemail.html",data)
def Emailverification(request):
    Email = request.GET['email']
    otp = request.GET['OTP']
    cursor = connection.cursor()
    query1 = "select * from users where email = '" + Email + "'"
    cursor.execute(query1)
    data = cursor.fetchone()
    if data is not None:
        if data[8] == otp:
            query2 = "update users set is_verify = 1 where email = '" + Email + "'"
            cursor.execute(query2)
            if cursor.rowcount == 1:
                print("otp verified successfully")
                data = {"email": "Email verification successsfull"}
                return render(request, "verified.html", data)
        else:
            data = {"email": "otp is not correct"}
            return render(request,"verified.html",data)
def ResetPassword(request):
    return render(request,"ResetPassword.html")
def changepassword(request):
    Email = request.GET['email']
    oldpassword = request.GET['oldpassword']
    newpassword = request.GET['newpassword']
    cursor = connection.cursor()
    query = "select * from users where email = '" + Email + "'"
    cursor.execute(query)
    data = cursor.fetchone()
    if data is not None:
        if data[5] == oldpassword:
            query1 = "update users set password='" + newpassword + "' where email = '" + Email +"'"
            cursor.execute(query1)
            data1 = cursor.fetchone()
            data1 ={"Changedpassword" : "password Changed Successfully"}
            return render(request,"Changedpassword.html",data1)
        else:
            data1 = {"Changedpassword": "password not correct"}
            return render(request, "Changedpassword.html", data1)





def loginpage_d(request):
    Email = request.GET['Email']
    Password = request.GET['psw']
    cursor = connection.cursor()
    query = "select * from users where email = '" + Email + "'"
    cursor.execute(query)
    data = cursor.fetchone()

    if data is not None:
        if Email == data[3] and Password == data[5]:
            data = {"message": "SignedUp"}
            return render(request,"message.html",data)
        else:
            data = {"message": "Not SignedUp"}
            return render(request, "message.html", data)

    else:
        data = {"message": "Not SignedUp"}
        return render(request, "message.html", data)

