from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import gettext_lazy as _

{% if cookiecutter.app_type == "UUID" %}
import uuid
{% elif cookiecutter.app_type == "Slug" %}
from autoslug import AutoSlugField
{% endif %}




class {{ cookiecutter.model_name }}(models.Model):
    { % if cookiecutter.app_type == "UUID" %}
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    { % endif %}
    name = models.CharField(max_length=255)
    { % if cookiecutter.app_type == "Slug" %}
    slug = AutoSlugField(populate_from='name', blank=True, editable=True,)
    { % endif %}

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ('-created', )

    def __unicode__(self):
        { % if cookiecutter.app_type == "UUID" %}
        return f'{self.name} ({self.id}'
        { % elif cookiecutter.app_type == "Slug" %}
        return self.slug
        { % endif %}

    def get_absolute_url(self):
        { % if cookiecutter.app_type == "UUID" %}
        return reverse('{{ cookiecutter.app_name }}_{{ cookiecutter.model_name|lower }}_read', args=(self.id, ))
        { % elif cookiecutter.app_type == "Slug" %}
        return reverse('{{ cookiecutter.app_name }}_{{ cookiecutter.model_name|lower }}_read', args=(self.slug, ))
        { % endif %}
