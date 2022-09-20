
from gettext import lngettext
from pickletools import read_bytes1
import re
from tokenize import Pointfloat
from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout

from datetime import date

# from django.core.mail import send_mail


# Create your views here.

def home(request):

    return render(request, 'home.html')

# Latest Scholarship view here
def latest_scholarships(request):

    allscholarship = AddScholarship.objects.all().order_by('-startdate')

    dic = {'AllScholarship': allscholarship}

    return render(request, 'latest_scholarships.html', dic)
#----------------------------------------------------
#               ADMIN
#----------------------------------------------------

# admin login page here:
def admin_login(request):

    
    error=""

    if request.method == "POST":
        
        uName = request.POST['uname']
        pwd = request.POST['psw']

        ADMIN = authenticate(username=uName, password=pwd)

        try:
            if ADMIN.is_staff:
                login(request, ADMIN)
                error="no"
        
        except:
            error="yes"

    dict = {'Error': error}

    return render(request, 'admin_login.html', dict)

# Admin Home Page here:
def admin_home(request):

    if not request.user.is_authenticated:
        return redirect('admin_login')

    return render(request, 'admin_home.html')

# Admin can change  Password 
def change_passwordadmin(request):

    
    error=""

    if request.method == "POST":

        currentpwd = request.POST['currentpass']
        newpwd = request.POST['conformpass']

        try:
            adminuser=User.objects.get(id=request.user.id)
            if adminuser.check_password(currentpwd):
                adminuser.set_password(newpwd) 
                adminuser.save()
                error="no"

            else:
                error="not"
        except:
            error="yes"
    
    dic = {'Error': error }
    return render(request, 'change_passwordadmin.html', dic)


# View Users Page in admin_home:
def view_users(request):

    if not request.user.is_authenticated:
        return redirect('admin_login')

    studentdata = StudentUser.objects.all()

    dic = {'userdata': studentdata}


    return render(request, 'view_users.html', dic)

# Delete User Page by admin:
def delete_user(request, uid):

    if not request.user.is_authenticated:
        return redirect('admin_login')

    studentrecord = User.objects.get(id=uid)
    studentrecord.delete()

    return redirect('view_users')

# Pending prvider ststus Page in admin_home:
def providers_pending(request):

    if not request.user.is_authenticated:
        return redirect('admin_login')

    providerdata = Provider.objects.filter(status="pending")

    dic = {'Providerdata': providerdata}

    return render(request, 'providers_pending.html', dic)


# Accepted prvider ststus Page in admin_home:
def providers_accepted(request):
    
    if not request.user.is_authenticated:
        return redirect('admin_login')

    providerdata = Provider.objects.filter(status="accept")

    dic = {'Providerdata': providerdata}

    return render(request, 'providers_accepted.html', dic)


# Rejected prvider ststus Page in admin_home:
def providers_rejected(request):
    
    if not request.user.is_authenticated:
        return redirect('admin_login')

    providerdata = Provider.objects.filter(status="reject")

    dic = {'Providerdata': providerdata}

    return render(request, 'providers_rejected.html', dic)


# Rejected prvider ststus Page in admin_home:
def providers_all(request):
    
    if not request.user.is_authenticated:
        return redirect('admin_login')

    providerdata = Provider.objects.all()

    dic = {'Providerdata': providerdata}

    return render(request, 'providers_all.html', dic)


# Change provider Pending ststus Page in admin_home:
def change_status(request, sid):

    if not request.user.is_authenticated:
        return redirect('admin_login')

    error=""

    providerstastus = Provider.objects.get(id=sid)

    if request.method == "POST":
        p_ststus = request.POST['status']

        providerstastus.status = p_ststus
    
        try:
            providerstastus.save()
            error = "no"
        except:
            error="yes"

    dic = {'Providerststus': providerstastus, 'Error': error}

    return render(request, 'change_status.html', dic)

# Delete Provider Page by admin:
def delete_provider(request, pid):

    if not request.user.is_authenticated:
        return redirect('admin_login')

    providerrecord = User.objects.get(id=pid)
    providerrecord.delete()

    return redirect('providers_all')

#----------------------------------------------------
#               SCHOLARSHIP PROVIDER
#----------------------------------------------------

# Privider sign-up here:
def provider_signup(request):

    error=""

    if request.method == "POST":

        fName = request.POST['fname']
        LName = request.POST['lname']
        comp = request.POST['company']
        phone = request.POST['contact']
        Email = request.POST['email']
        pwd = request.POST['psw']
        gen = request.POST['Radios']
        img = request.FILES['image']

        try:
            USER = User.objects.create_user(first_name=fName, last_name=LName, username=Email, password=pwd)
            Provider.objects.create(user=USER, mobile=phone, gender=gen, image=img, companyname=comp, usertype="provider", status="pending")
            error= "no"

        except:
            error= "yes"
    
    dic = {'Error': error}
    return render(request, 'provider_signup.html', dic)

# Privider Login here:
def provider_login(request):

    error=""

    if request.method == "POST":

        uName = request.POST['uname']
        pwd = request.POST['psw']

        PROVIDER = authenticate(username=uName, password=pwd)

        if PROVIDER:
            # error="no"
            try:
                providerdata = Provider.objects.get(user=PROVIDER)
                
                if providerdata.usertype == "provider" and providerdata.status != "pending" and providerdata.status != "Reject":
                    login(request, PROVIDER)
                    error="no"
                else:
                    error="not"
            except:
                error="yes"
        else:
            error="yes"
       
    dict = {'Error': error}

    return render(request, 'provider_login.html', dict) 

# Provider Home Page here:
def provider_home(request):

    if not request.user.is_authenticated:
        return redirect('provider_login')
    
    USER = request.user
    PROVIDER = Provider.objects.get(user=USER)

    error=""

    if request.method == "POST":

        fName = request.POST['fname']
        LName = request.POST['lname']
        comp = request.POST['company']
        phone = request.POST['contact']
        gen = request.POST['Radios']

        PROVIDER.user.first_name = fName
        PROVIDER.user.last_name = LName
        PROVIDER.mobile = phone
        PROVIDER.companyname = comp
        PROVIDER.gender = gen

        try:
            PROVIDER.save()
            PROVIDER.user.save()
            error= "no"
        except:
            error= "yes"

        try:
            img = request.FILES['image']
            PROVIDER.image = img
            PROVIDER.save()
            error= "no"
        except:
            pass
    dic={'Error': error, 'Provider': PROVIDER}

    return render(request, 'provider_home.html', dic)


# Provider Home Page here:
def add_scholarship(request):

    if not request.user.is_authenticated:
        return redirect('provider_login')

    error=""

    if request.method == "POST":

        Title = request.POST['title']
        startDate = request.POST['startdate']
        endDate = request.POST['enddate']
        Income = request.POST['income']
        Type = request.POST['type']
        Marks = request.POST['marks']
        no = request.POST['nofscholarship']
        Location=request.POST['location']
        Logo = request.FILES['logo']
        Form = request.FILES['forms']
        disc = request.POST['discription']
        USER=request.user
        PROVIDER = Provider.objects.get(user=USER)

        try:
            AddScholarship.objects.create(provider=PROVIDER, title=Title, startdate=startDate, 
            enddate=endDate, income=Income, scholarshiptype=Type, noofscholarships=no, logo=Logo, 
            prviousmarks=Marks, Location=Location, discription=disc, scholarshipform=Form, createdate=date.today())
            error= "no"

        except:
            error= "yes"
    
    dic = {'Error': error}

    return render(request, 'add_scholarship.html', dic)

# Scholarship List Page here:
def scholarship_list(request):

    if not request.user.is_authenticated:
        return redirect('provider_login')

    USER = request.user
    PROVIDER = Provider.objects.get(user=USER)
    SCHOLARSHIP = AddScholarship.objects.filter(provider=PROVIDER)

    dic={'scholarship': SCHOLARSHIP}
    return render(request, 'scholarship_list.html', dic)

# Edit Schilarship details by provider
def edit_scholarshipdetails(request, eid):
    
    if not request.user.is_authenticated:
        return redirect('provider_login')

    error=""
    editscholarship = AddScholarship.objects.get(id=eid)
    if request.method == "POST":

        Title = request.POST['title']
        startDate = request.POST['startdate']
        endDate = request.POST['enddate']
        Income = request.POST['income']
        Type = request.POST['type']
        Marks = request.POST['marks']
        no = request.POST['nofscholarship']
        Location=request.POST['location']
        disc = request.POST['discription']
        
        editscholarship.title = Title
        editscholarship.income = Income
        editscholarship.scholarshiptype = Type
        editscholarship.noofscholarships = no
        editscholarship.prviousmarks=Marks
        editscholarship.Location=Location
        editscholarship. discription=disc



        try:
            editscholarship.save()
            error="no"

        except:
            error= "yes"

        if startDate:
            try:
                editscholarship.startdate = startDate
                editscholarship.save()
            except:
                pass
        else:
            pass

        if endDate:
            try:
                editscholarship.enddate = endDate
                editscholarship.save()
            except:
                pass
        else:
            pass

        
        try:
            Logo = request.FILES['logo']
            editscholarship.logo = Logo
            editscholarship.save()
        except:
            pass

        try:
            Form = request.FILES['forms']
            editscholarship.scholarshipform = Form
            editscholarship.save()
        except:
            pass
        

            

    
    dic = {'Error': error, 'EditScholarship': editscholarship}

    return render(request, 'edit_scholarshipdetails.html', dic)

# delete Add Scholarship by provider
def delete_addscholarship(request, aid):
    
    if not request.user.is_authenticated:
        return redirect('provider_login')

    scholarshipdata = User.objects.get(id=aid)
    scholarshipdata.delete()

    return redirect('scholarship_list')

# Provider user can change  Password 
def change_passwordprovider(request):

    error=""

    if request.method == "POST":

        currentpwd = request.POST['currentpass']
        newpwd = request.POST['conformpass']

        try:
            provideruser=User.objects.get(id=request.user.id)
            if provideruser.check_password(currentpwd):
                provideruser.set_password(newpwd) 
                provideruser.save()
                error="no"

            else:
                error="not"
        except:
            error="yes"
    
    dic = {'Error': error }
    return render(request, 'change_passwordprovider.html', dic)


# Scholarship List Page here:
def applied_candidates(request):

    if not request.user.is_authenticated:
        return redirect('provider_login')

 
    Applied = ApplyScholarship.objects.all()

    dic={'AppliedCandidates': Applied}
    return render(request, 'applied_candidates.html', dic)

#  Students whole details view by provider here
def user_details(request, pid):

    if not request.user.is_authenticated:
        return redirect('provider_login')

    Applieduser = ApplyScholarship.objects.get(id=pid)


    dic = {'applieduser': Applieduser}

    return render(request, 'user_details.html', dic)

#----------------------------------------------------
#               STUDENT USER
#----------------------------------------------------
# Student Signup here:
def user_signup(request):

    error=""

    if request.method == "POST":

        fName = request.POST['fname']
        LName = request.POST['lname']
        phone = request.POST['contact']
        Email = request.POST['email']
        pwd = request.POST['psw']
        gen = request.POST['Radios']
        img = request.FILES['image']

        try:
            USER = User.objects.create_user(first_name=fName, last_name=LName, username=Email, password=pwd)
            StudentUser.objects.create(user=USER, mobile=phone, gender=gen, image=img, usertype="student")
            error= "no"

        except:
            error= "yes"
    
    dic = {'Error': error}
    return render(request, 'user_signup.html', dic)


# Student Login here:
def user_login(request):

    error=""

    if request.method == "POST":

        uName = request.POST['uname']
        pwd = request.POST['psw']

        USER = authenticate(username=uName, password=pwd)

        if USER:
            # error="no"
            try:
                userdata = StudentUser.objects.get(user=USER)
                
                if userdata.usertype == "student":
                    login(request, USER)
                    error="no"
                else:
                    error="yes"
            except:
                error="yes"
        else:
            error="yes"
       
    dict = {'Error': error}

    return render(request, 'user_login.html', dict)

# Student Home Page here:
def user_home(request):

    if not request.user.is_authenticated:
        return redirect('user_login')
    
    USER = request.user
    STUDENT = StudentUser.objects.get(user=USER)
    error=""

    if request.method == "POST":

        fName = request.POST['fname']
        LName = request.POST['lname']
        phone = request.POST['contact']
        gen = request.POST['Radios']
        Degree = request.POST['degree']
        Marks = request.POST['marks']
        Income = request.POST['income']
        Location = request.POST['location']
        disc = request.POST['discription']

        STUDENT.user.first_name = fName
        STUDENT.user.last_name = LName
        STUDENT.mobile = phone
        STUDENT.gender = gen
        STUDENT.currentdegree = Degree
        STUDENT.previousmarks = Marks
        STUDENT.income = Income
        STUDENT.location = Location
        STUDENT.discriotion = disc







        try:
            STUDENT.save()
            STUDENT.user.save()
            error = "no"

        except:
            error= "yes"

        try:
            img = request.FILES['image']
            STUDENT.image = img
            STUDENT.save()
            error="no"
        except:
            pass
    
    dic = {'Error': error, 'Student': STUDENT}

    return render(request, 'user_home.html', dic)


# Student user can change  Password 
def change_passworduser(request):

    if not request.user.is_authenticated:
        return redirect('user_login')

    error=""

    if request.method == "POST":

        currentpwd = request.POST['currentpass']
        newpwd = request.POST['conformpass']

        try:
            studentuser=User.objects.get(id=request.user.id)
            if studentuser.check_password(currentpwd):
                studentuser.set_password(newpwd) 
                studentuser.save()
                error="no"

            else:
                error="not"
        except:
            error="yes"
    
    dic = {'Error': error }
    return render(request, 'change_passworduser.html', dic)

#User Latest Scholarship view here
def user_latestscholarships(request):

    if not request.user.is_authenticated:
        return redirect('user_login')

    allscholarship = AddScholarship.objects.all().order_by('-startdate')

    USER = request.user
    STUDENT = StudentUser.objects.get(user=USER)
    applystudent = ApplyScholarship.objects.filter(student=STUDENT)

    List=[]

    for data in applystudent:
        List.append(data.addscholarship.id)


    dic = {'AllScholarship': allscholarship, 'List':List}

    return render(request, 'user_latestscholarships.html', dic)


#  Scholarship whole details view here
def scholarship_details(request, pid):

    if not request.user.is_authenticated:
        return redirect('user_login')

    scholarship = AddScholarship.objects.get(id=pid)


    dic = {'ScholarshipId': scholarship}

    return render(request, 'scholarship_details.html', dic)

#  Apply for scholarship view here
def applyforscholarship(request, pid):

    if not request.user.is_authenticated:
        return redirect('user_login')
    error = ""

    USER = request.user
    STUDENT = StudentUser.objects.get(user=USER)
    SCHOLARSHIP = AddScholarship.objects.get(id=pid)

    currentdate = date.today()

    if SCHOLARSHIP.enddate < currentdate:
        error = 'closed'
    elif SCHOLARSHIP.startdate > currentdate:
        error = 'notopend'
    
    else:
        try:
            if request.method == "POST":
                Form = request.FILES['forms']

                ApplyScholarship.objects.create(addscholarship=SCHOLARSHIP, student=STUDENT, scholarshipform=Form, applyeddate=date.today())
                error = 'done'
        except:
            error = 'no'


    dic = {'Error': error, 'Applyed': STUDENT}

    return render(request, 'applyforscholarship.html', dic)
#----------------------------------------------------
#          LOG OUT FUNCTION
#----------------------------------------------------

# Log-out Function Here:
def Logout(request):
    logout(request)
    return redirect('home')