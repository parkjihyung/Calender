from django.db import models

# Create your models here.
import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

# After writing models.py file, execute the follow command
# py manage.py makemigrations polls

# If you execute the follow command, the tables of models will be created.
# py manage.py migrate

# insert a data into Question Model
# py manage.py shell
# >>> from polls.models import Choice, Question
# >>> Question.objects.all()
# >>> from django.utils import timezone
# >>> from django.utils import timezone
# >>> q = Question(question_text="What is new?", pub_date=timezone.now())
# >>> q.save()
# >>> q.id
# >>> Question.objects.get(id=1)


class Calendar(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    start = models.DateTimeField('Start Date')
    end = models.DateTimeField('End Date')
    allDay = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title