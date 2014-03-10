from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.forms import TextInput, Textarea
from textile.functions import textile
from m_cmsplugin_labs.models import Lab, Task
from django.contrib import admin
from django.db import models


class LabTaskInline(admin.TabularInline):
    model = Task
    extra = 1
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
        models.TextField: {'widget': Textarea(attrs={'rows': '4', 'cols': '60'})},
    }
    fieldsets = [
        (None, {'fields': ['task_number', 'description', 'complexity']}),
        ('User info', {'fields': ['selected', 'user'], 'classes': ['collapse', ]}),
    ]
    fk_name = 'lab'


def textile_without_p(text):
    text = textile(text)
    return text[4:-4]


class LabsPlugin(CMSPluginBase):
    name = u"Lab tasks list"
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': '4', 'cols': '80'})},
    }

    model = Lab
    render_template = "m_cmsplugin_labs/lab.html"
    text_enabled = True
    inlines = [LabTaskInline]

    def render(self, context, instance, placeholder):
        instance.description = textile_without_p(instance.description)

        tasks = list(Task(description=textile_without_p(t.description),
                          complexity=t.complexity,
                          selected=t.selected,
                          user=t.user,
                          task_number=t.task_number) for t in instance.task_set.all())

        context['tasks'] = tasks
        context['lab'] = instance
        return context


plugin_pool.register_plugin(LabsPlugin)