from django.db import models
from accounts.models import TimestampedModel
from accounts.models import User


class Questions(TimestampedModel):
    """
   Question and Answer model
    """
    mentor=models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentor', null=True, blank=True)
    question = models.CharField(max_length=1000,help_text='Question', null=True, blank=True)
    answer = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='attachments', null=True, blank=True)
    
    def __str__(self):
        return self.question

