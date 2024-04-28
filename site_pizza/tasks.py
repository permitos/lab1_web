from celery import shared_task
from celery.schedules import crontab
from celery import periodic_task
from django.utils import timezone
from .models import BlogPost
from datetime import timedelta

@shared_task
def check_publication_date():
    half_year_ago = timezone.now() - timezone.timedelta(days=180)
    outdated_posts = BlogPost.objects.order_by("-public_date")
    for post in outdated_posts:
        if post.public_date < half_year_ago:
            post.actual_status = False

@periodic_task(run_every=timedelta(days=1))
def check_publication_dates_task():
    check_publication_date.delay()