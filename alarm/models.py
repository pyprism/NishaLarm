from django.db import models


class Api(models.Model):
    account_sid = models.CharField(max_length=50)
    auth_token = models.CharField(max_length=50)
    from_number = models.CharField(max_length=30)
    to_number = models.CharField(max_length=30)

    def __str__(self):
        return str(self.account_sid)


class Nisha(models.Model):
    time = models.DateField()
    snooze = models.BooleanField(default=False)
    repeat_time = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.time, self.done
