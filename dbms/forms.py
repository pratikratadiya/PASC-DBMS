from django.core.exceptions import ValidationError                          # Validation Error method 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm      # Using django's predefined forms
from .models import user

# Form for creating new user 
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = user                                        # using the user model
        fields = ('username', 'email', 'event')
        help_texts = {'username':(''), 'email':(''), 'event':(''),}

# Form to change information of existing user    	    	
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = user
        fields = ('event',)