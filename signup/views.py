from django.shortcuts import render
from .forms import RegisterForm
from .models import User_Profile
from django.core.context_processors import csrf
from django.contrib import messages
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.contrib.auth.hashers import make_password,check_password
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
# Create your views here.

# Method calls the register.html form allowing user to enter his personal information       
# Method calls the register.html form allowing user to enter his personal information       
def register(request):
    context = {"form" : RegisterForm()}
    context.update(csrf(request))
    template = "student_register.html"
    return render_to_response("student_register.html",context ,context_instance = RequestContext(request))


# Method allows the user to enter the information and submit
def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        try :
            if form.is_valid():
                email = form.cleaned_data['email']
                location = form.cleaned_data['location']
                phone = form.cleaned_data['phone']
                promo_code = form.cleaned_data['promo_code']
                new_user = User.objects.create_user(email,
                                        form.cleaned_data['password'])
                new_user.first_name = form.cleaned_data['first_name']
                new_user.last_name = form.cleaned_data['last_name']
                new_user.email = email
                new_user.save()
                    
                new_form = User_Profile(user=new_user,phone=phone,promo_code=promo_code,location=location)
                new_form.save()
                return HttpResponseRedirect('/')
            else :
                print "erroorrrrrr",form.errors
                messages.error(request, "There is an error in your submission!")
        except IntegrityError:
            messages.error(request, "The email you entered already exists!")
    else : form = RegisterForm()
    context = {"form" : form}
    template = "student_register.html"     
    return render_to_response(template,context, context_instance = RequestContext(request))


