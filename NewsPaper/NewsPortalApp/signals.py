# from django.conf import settings
# from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
# from django.template.loader import render_to_string
# from django.core.mail import EmailMultiAlternatives

from NewsPortalApp.models import PostCategory
from .tasks import send_notifications


@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.category.all()
        subscribers: list[str] = []
        for category in categories:
            subscribers += category.subscribers.all()

        subscribers = [s.email for s in subscribers]

        send_notifications.apply_async(
            (instance.preview(), instance.pk, instance.header, subscribers))

