import re
import json

from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.http import JsonResponse


from allauth.account.views import SignupView, LoginView
from django.contrib.auth.decorators import login_required

from smtplib import SMTPException
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError, PermissionDenied
from django.conf import settings
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.core.validators import validate_email
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.translation import gettext_lazy as _



from .models import *


User = get_user_model()


@login_required
def home_view(request):
	return HttpResponse("hi")



class ClientSignupView(SignupView):
    def dispatch(self, request, *args, **kwargs):
        if request.method == "GET":
            response = super(ClientSignupView, self).dispatch(request, *args, **kwargs)
            return response
        elif request.method == "POST":
            existing_users = User.objects.all()
            existing_usernames = existing_users.values_list("username", flat=True)
            existing_emails = existing_users.values_list("email", flat=True)
            username = request.POST.get("username")
            email = request.POST.get("email")
            password_1 = request.POST.get("password1")
            password_2 = request.POST.get("password2")

            if not username:
                messages.error(request, _("Please provide username!"))
            elif not email:
                messages.error(request,  _("Please provide email address!"))
            elif not password_1:
                messages.error(request,  _("Please enter password!"))
            elif not password_2:
                messages.error(request,  _("Please confirm the password!"))

            if username:
                username_pattern = re.compile(r"^[a-zA-Z\d_-]+$")
                if username in existing_usernames:
                    messages.error(request,  _("Username already exists!"))
                elif not bool(username_pattern.match(username)):
                    messages.error(request,  _("Username can contain only letters, digits, hyphen(-) and underscore(_)"))
                elif len(username) > 120:
                    messages.error(request,  _("Username can't be more than 120 characters!"))

            if email:
                try:
                    validate_email(email)
                except ValidationError:
                    messages.error(request,  _("Please enter a valid email address!"))

                if email in existing_emails:
                    messages.error(request,  _("An account with this email already exists!"))
                elif username and (email == username):
                    messages.error(request,  _("Email and username can't be the same!"))

            if password_1 and password_2:
                if password_1 != password_2:
                    messages.error(request,  _("Passwords don't match!"))
                else:
                    pass
            if request.POST.get("remember-me") is None:
                self.request.session.set_expiry(0)
                
            response = super(ClientSignupView, self).dispatch(request, *args, **kwargs)
            return response
    template_name = "account/signup.html"


class ClientSigninView(LoginView):
    def dispatch(self, request, *args, **kwargs):
        if request.method == "GET":
            response = super(ClientSigninView, self).dispatch(request, *args, **kwargs)
            return response
        elif request.method == "POST":
            username = request.POST.get("login")
            password = request.POST.get("password")

            if not username:
                messages.error(request, _("Please enter username / email!"))
            if not password:
                messages.error(request, _("Please enter password!"))
            if username and password:
                user = User.objects.filter(username=username).first()
                if not user:
                    user = User.objects.filter(email=username).first()
                    messages.error(request, _("Username or email is incorrect!"))
                elif not user.check_password(password):
                    messages.error(request, _("Password is incorrect!"))
                if request.POST.get("remember") is None:
                    self.request.session.set_expiry(0)
        response = super(ClientSigninView, self).dispatch(request, *args, **kwargs)
        return response
    def get_context_data(self, *args, **kwargs):
        context = {}
        context = super(ClientSigninView, self).get_context_data(*args,**kwargs)
        # try:
        #     context['contact'] = Contact.objects.all()[0]
        # except:
        #     pass
        return context
    template_name = "account/signin.html"




def server_error(request):
    return render(request, "500.html")