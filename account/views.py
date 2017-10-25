from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate

from account.forms import RegistrationForm


class RegisterView(TemplateView):
    """Registration view

    View class for Sign Up

    """
    
    template_name = "register.html"
    form_class = RegistrationForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect(reverse('home'))
        form = self.form_class(None, request.POST or None)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
        return render(request, self.template_name, {'form': form})
