import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

# Create your models here.
class UserTask(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey("users.User", verbose_name=_("User"), on_delete=models.CASCADE)
    task = models.CharField(_("Task"), max_length=500)
    date = models.DateField(_("Date Added"), auto_now_add=True)

    class Meta:
        verbose_name = _("usertask")
        verbose_name_plural = _("usertasks")

    def __str__(self):
        return self.task

    def get_absolute_url(self):
        return reverse("usertask_detail", kwargs={"pk": self.pk})
