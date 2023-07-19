# Send email on successful register: Variant 3
# Best one
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from core.email_utils import send_email_with_template

UserModel = get_user_model()

'''
Other text
<div class='ala-bala' id='root' disabled=true data-value="5" .... >
    Some text
</div>
after text

=> strip_tags(...)

Other text
Some text
after text
'''


def send_successful_registration_email(user):
    context = {
        'user': user,
    }
    send_email_with_template(
        subject='Registration greetings',
        template_name='emails/email-greeting.html',
        context=context,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=(user.email,)
    )


@receiver(post_save, sender=UserModel)
def user_created(instance, created, **kwargs):
    if created:
        send_successful_registration_email(instance)
