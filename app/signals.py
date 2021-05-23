from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch.dispatcher import receiver


@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print("----------------")
    print("Logged-in Signal... Run Intro..")
    print("Sender:", sender)
    print("Request:", request)
    print("User:", user)
    print("User Password:", user.password)
    print(f'Kwargs: {kwargs}')


# user_logged_in.connect(login_success, sender=User)
@receiver(user_logged_out, sender=User)
def login_out(sender, request, user, **kwargs):
    print("----------------")
    print("Logged-out Signal... Run Outro..")
    print("Sender:", sender)
    print("Request:", request)
    print("User:", user)
    print(f'Kwargs: {kwargs}')


@receiver(user_login_failed)
def login_failed(sender, credentials , request, **kwargs):
    print("----------------")
    print("Logged failed Signal...")
    print("Sender:", sender)
    print("Credentials:", credentials)
    print("Request:", request)
    print(f'Kwargs: {kwargs}')