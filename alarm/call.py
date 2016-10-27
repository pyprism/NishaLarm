import django
import os
from twilio.rest import TwilioRestClient

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hiren.settings")
django.setup()

from alarm.models import Nisha, Api


def hiren():
    bunny = Api.objects.all()
    print(bunny[0])
    client = TwilioRestClient(bunny[0].account_sid, bunny[0].auth_token)


hiren()