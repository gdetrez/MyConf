from django.db import models
from schedule.models import Session

# Create your models here.

class SessionSignup(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField( help_text = "Note that it should be the same email address you used when you registered for the conference." )
    date = models.DateTimeField(auto_now=True)
 
    session = models.ForeignKey(Session)
    
    class Meta:
        unique_together = (("email", "session"),)
