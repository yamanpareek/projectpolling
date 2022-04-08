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
    query = "select * from users where email = '" + Email + "'"
    cursor.execute(query)
    data = cursor.fetchall()

    if len(data) > 0:
        msg = {"message": "you already registered please try login"}
        return render(request, "message.html", msg)

    else:

        query = "insert into users (fullname , age , email , phonenumber , password , gender ) values (%s , %s, %s , %s , %s , %s)"
        value = (FullName, Age, Email, PhoneNumber, Password, Gender)
        cursor.execute(query, value)
        data = {"message": "SignedUp", "email": Email}
        return render(request, "user_panel.html", data)


def loginpage_d(request):
    Email = request.GET['Email']
    Password = request.GET['psw']
    cursor = connection.cursor()
    query1 = "select * from users where email = '" + Email + "'"
    cursor.execute(query1)
    data = cursor.fetchone()

    if data is not None:
        if Email == data[3] and Password == data[5]:
            query1 = "select * from poll where email='" + Email + "'"
            cursor.execute(query1)
            data = cursor.fetchall()
            data = {"data": data, "email": Email}
            return render(request, "user_panel.html", data)
        else:
            data = {"message": "Not SignedUp"}
            return render(request, "message.html", data)

    else:
        data = {"message": "Not SignedUp"}
        return render(request, "message.html", data)


def create_poll(request):
    email = request.GET['email']
    data = {"email": email}
    return render(request, "create_poll.html", data)


def poll(request):
    email = request.GET['email']
    poll_title = request.GET['poll_title']
    opt1 = request.GET['opt1']
    opt2 = request.GET['opt2']
    opt3 = request.GET['opt3']
    opt4 = request.GET['opt4']
    cursor = connection.cursor()
    query1 = "select * from poll where email = '" + email + "' and poll_title = '" + poll_title + "'"
    cursor.execute(query1)
    data1 = cursor.fetchall()
    if len(data1) > 0:
        data2 = {"message": "poll already exist....!"}
        return render(request, "message.html", data2)
    query2 = "insert into poll(email,poll_title,option1,op1_value, option2,op2_value, option3,op3_value, option4,op4_value) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    value = (email, poll_title, opt1, 0, opt2, 0, opt3, 0, opt4, 0)
    cursor.execute(query2, value)
    data3 = {'poll_title': poll_title, 'opt1': opt1, 'opt2': opt2, 'opt3': opt3, 'opt4': opt4, 'email': email}
    return render(request, "poll.html", data3)


def poll_result(request):
    table_struct = ['id', 'email', 'poll_title', 'option1', 'op1_value', 'option2', 'op2_value', 'option3', 'op3_value',
                    'option4', 'op4_value']
    email = request.GET['email']
    poll_title = request.GET['poll_title']
    option = request.GET['option']
    flag = 2
    for col in range(4, len(table_struct), 2):
        flag += 2
        if table_struct[col] == option:
            break

    cursor = connection.cursor()
    if flag == 4:
        query = "select op1_value from poll where email = '" + email + "' and poll_title = '" + poll_title + "'"
        cursor.execute(query)
        data = cursor.fetchone()
        value = int(data[0])
        value += 1
        query1 = "update poll set op1_value = %s where email = '" + email + "' and poll_title = '" + poll_title + "'"
        value1 = (value,)
        cursor.execute(query1, value1)
    elif flag == 6:
        query = "select op2_value from poll where email = '" + email + "' and poll_title = '" + poll_title + "'"
        cursor.execute(query)
        data = cursor.fetchone()
        value = int(data[0])
        value += 1
        query1 = "update poll set op2_value = %s where email = '" + email + "' and poll_title = '" + poll_title + "'"
        value1 = (value,)
        cursor.execute(query1, value1)
    elif flag == 8:
        query = "select op3_value from poll where email = '" + email + "' and poll_title = '" + poll_title + "'"
        cursor.execute(query)
        data = cursor.fetchone()
        value = int(data[0])
        value += 1
        query1 = "update poll set op3_value =%s where email = '" + email + "' and poll_title = '" + poll_title + "'"
        value1 = (value,)
        cursor.execute(query1, value1)
    else:
        query = "select op4_value from poll where email = '" + email + "' and poll_title = '" + poll_title + "'"
        cursor.execute(query)
        data = cursor.fetchone()
        value = int(data[0])
        value += 1
        query1 = "update poll set op4_value =%s  where email = '" + email + "' and poll_title = '" + poll_title + "'"
        value1 = (value,)
        cursor.execute(query1, value1)
    query3 = "select * from poll where email='" + email + "' and poll_title= '" + poll_title + "'"
    cursor.execute(query3)
    data = cursor.fetchall()
    data = {"data": data, "email": email}
    return render(request, "result.html", data)
