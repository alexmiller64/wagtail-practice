from django.db import models

from wagtail.core.models import Page

from wagtail.contrib.settings.models import BaseSetting, register_setting

from modelcluster.fields import ParentalKey
from wagtail.core.models import Page, Orderable
from django.db.models import Q
from wagtail.documents.models import Document
from wagtail.documents.edit_handlers import DocumentChooserPanel


from datetime import date, datetime
from wagtail.images.models import Image
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel, StreamFieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.contrib.settings.models import BaseSetting, register_setting

class HomePage(Page):
    main_hero_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    hero_heading = models.CharField(max_length=255, null=True, blank=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('main_hero_image'),
        FieldPanel('hero_heading'),
    ]

@register_setting
class SocialMediaSettings(BaseSetting):
    facebook = models.URLField(
        help_text='Your Facebook page URL')
    instagram = models.CharField(
        max_length=255, help_text='Your Instagram username, without the @')
    trip_advisor = models.URLField(
        help_text='Your Trip Advisor page URL')
    youtube = models.URLField(
        help_text='Your YouTube channel or user account URL')    

