'''
Created on 06/03/2015

@author: dam201
'''
from Almar.models import Usuario
from django.conf import settings
from django.contrib.auth.models import User, check_password
 
class SettingsBackend(object):
    """
    Authenticate against the settings ADMIN_LOGIN and ADMIN_PASSWORD.
 
    Use the login name, and a hash of the password. For example:
 
    ADMIN_LOGIN = 'admin'
    ADMIN_PASSWORD = 'sha1$4e987$afbcf42e21bd417fb71db8c66b321e9fc33051de'
    """
    def authenticate(self, username=None, password=None):

        try:
            user = Usuario.objects.get(nombre = username)
            #user_pass = Usuario.objects.get(password = password)
            return user
        except Usuario.DoesNotExist:
            user = User(username=username, password=password)
            user.is_staff = True
            user.is_superuser = False
            user.save()
            
        return None
    def get_user(self, user_id):
        try:
            return Usuario.objects.get(pk=user_id)
        except Usuario.DoesNotExist:
            return None