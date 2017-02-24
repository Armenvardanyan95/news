from celery import Celery
from django.conf import settings
from magazines.models import Magazine
from utils.general import generate_randomizer

app = Celery('news', broker=settings.BROKER_URL)

@app.task
def re_randomize_magazines():
    Magazine.objects.update(randomizer=generate_randomizer(Magazine))
