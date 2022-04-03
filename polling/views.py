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
        return render(request,"index.html")

    else:

        query = "insert into users (fullname , age , email , phonenumber , password , gender ) values (%s , %s, %s , %s , %s , %s)"
        value = (FullName, Age, Email, PhoneNumber, Password, Gender)
        cursor.execute(query, value)
        return render(request, "signuppage.html")


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
