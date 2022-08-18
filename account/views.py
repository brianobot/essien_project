from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from .forms import AuthenticationForm, CustomUserCreationForm

# Create your views here.
def sign_up_page(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:login-account')

    form = CustomUserCreationForm()
    return render(request, 'account/Sign-up.html')


class LoginPage(auth_views.LoginView):
    template_name = 'account/login.html'
    form_class = AuthenticationForm

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('library:home')
        return super().get(*args, **kwargs)


def logout_account(request):
    logout(request)
    return redirect('account:login-account')