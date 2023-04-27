from django.contrib import admin
from django.forms import ModelForm, ModelMultipleChoiceField
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.utils.translation import gettext_lazy as _

from .models import (
    Tag,
    Seed
)
# Register your models here.

admin.site.register(Tag)


class SeedForm(ModelForm):
    """
    SeedForm defines a form to be used in admin for adding seeds.
    """
    # Many choice field for tags m2m
    tags = ModelMultipleChoiceField(
        queryset=Tag.objects.filter(deleted=False),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name=_("Tags"),
            is_stacked=False
        )
    )

    def __init__(self, *args, **kwargs):
        super(SeedForm, self).__init__(*args, **kwargs)
        # Initialize the tags for field with already selected tags.
        if self.instance and self.instance.pk:
            self.fields["tags"].initial = self.instance.tags.all()

    class Meta:
        model = Seed
        exclude = ["id"]


@admin.register(Seed)
class SeedAdmin(admin.ModelAdmin):
    form = SeedForm
