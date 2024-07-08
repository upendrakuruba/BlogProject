from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from .forms import *

urlpatterns = [
    path("Signpage/", Sign_page, name="Signpage"),
    path("Loginpage/", Login_page, name="Login"),
    path("logout_user/", logout_user, name="logout_user"),
    path("download_csv/", download_csv, name="download_csv"),
    path("passwordchange/", auth_views.PasswordChangeView.as_view(template_name='accounts/changepassword.html',form_class=MyPasswordChangeForm,success_url='/passwordchangedone/'),name="passwordchange"),
    path("passwordchangedone/", auth_views.PasswordChangeDoneView.as_view(template_name='accounts/passwordchangedone.html'),name="passwordchangedone"),
    path("password-reset/", auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),name='password_reset_done'),
    path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),name='password_reset_complete'),

]
