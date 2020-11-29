
import smtplib
from email.mime.text import MIMEText
from django.conf import settings
try:
    from celery import shared_task
except ImportError:
    raise ImportError('you need to install celery and setup celery configuration')


from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

url = getattr(settings, 'FRONT_URL', '')


@shared_task
def send_register_mail(user, key):
    body = """
    Hello %s

    Confirmation Mail: %s

    You can see more details in this link: %s/account-confirm-email/%s <br><br>

    Thank you <br><br>
    <p>
    """% (user.first_name, user.email, url, key)
    
    subject = "Registeration Confirmation Mail"
    recipients = [user.email]
    
    #try:
    if True:
        send_email(body, subject, recipients, 'html')
        return "Email Is Sent"
    #except Exception as e:
        return "Email not sent"
        #print("Email not sent ", e)

@shared_task
def send_reset_password_email(user):
    body = """
    hello %s,

    Reset Mail Link : %s/%s/%s

    """ %(user.username, url, urlsafe_base64_encode(force_bytes(user.pk)),default_token_generator.make_token(user))
    subject = "Reset password Mail"
    recipients = [user.email]
    try:
        send_email(body, subject, recipients, 'html')
        return "Email Is Sent"
    except Exception as e:
        print("Email not sent ", e)



def send_email(body, subject, recipients, body_type='plain'):
    session = smtplib.SMTP('smtp.gmail.com', getattr(settings, 'EMAIL_PORT', 587))
    session.starttls()
    session.login(getattr(settings, 'EMAIL_HOST_USER', None), getattr(settings, 'EMAIL_HOST_PASSWORD', None))
    sender = getattr(settings, 'EMAIL_HOST_USER', None)
    msg = MIMEText(body, body_type)
    msg['subject'] = subject
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)
    session.sendmail(sender, recipients, msg.as_string())
