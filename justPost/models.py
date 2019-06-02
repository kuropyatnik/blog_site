from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about_me = models.CharField(max_length=250, null=True, blank=True)
    subscriptions = models.ManyToManyField('self', related_name='subscribers', symmetrical=False)
    viewed_posts = models.ManyToManyField('Posts', related_name='viewers', symmetrical=False)

    def str(self):
        return self.username


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Posts (models.Model):
    post_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    content = models.TextField(max_length=1000)

    class Meta:
        ordering = ['pub_date']

    def str(self):
        return self.title

