from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Lab(CMSPlugin):
    title = models.CharField(max_length=200, blank=True, default="")
    description = models.TextField(blank=True, default="")

    def __unicode__(self):
        return self.title

    def copy_relations(self, old_instance):
        for item in old_instance.task_set.all():
            item.pk = None
            item.lab = self
            item.save()

class Task(models.Model):
    UNDEFINED = ""
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"
    NIGHTMARE = "nightmare"

    COMPLEX_CHOICES = (
        (UNDEFINED, _("")),
        (EASY, _("Easy")),
        (MEDIUM, _("Medium")),
        (HARD, _("Hard")),
        (NIGHTMARE, _("Nightmare")),
    )

    lab = models.ForeignKey("Lab")

    task_number = models.IntegerField(default=1)

    description = models.TextField(blank=True, default="")

    complexity = models.CharField(max_length=20,
                                  choices=COMPLEX_CHOICES,
                                  default=EASY)

    selected = models.BooleanField(default=False)

    user = models.CharField(verbose_name="name of user",
                            max_length=100, blank=True, default="")

    def __unicode__(self):
        return self.user + " | " + self.description[:25]



    class Meta:
        ordering = ['task_number']



