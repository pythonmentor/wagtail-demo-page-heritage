from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel


class BaseEventPage(Page):
    """Page présentant un événement."""

    parent_page_types = []


class EventPage(BaseEventPage):
    """Page présentant un événement."""

    parent_page_types = ["home.EventIndexPage"]


class EventIndexPage(Page):
    """Page racine des événements."""

    parent_page_types = ["home.HomePage"]

    def get_context(self, request, *args, **kwargs):
        return {
            **super().get_context(request, *args, **kwargs),
            "events": EventPage.objects.child_of(self).live().specific(),
        }


class ColloquePage(BaseEventPage):
    """Page présentant un colloque"""

    parent_page_types = ["home.ColloqueIndexPage"]


class ColloqueIndexPage(Page):
    """Page racine des colloques."""

    parent_page_types = ["home.HomePage"]

    def get_context(self, request, *args, **kwargs):
        return {
            **super().get_context(request, *args, **kwargs),
            "colloques": ColloquePage.objects.child_of(self).live().specific(),
        }


class HomePage(Page):
    """Page d'accueil du site."""

    parent_page_types = ["wagtailcore.Page"]

    def get_context(self, request, *args, **kwargs):
        return {
            **super().get_context(request, *args, **kwargs),
            "items": BaseEventPage.objects.descendant_of(self)
            .live()
            .specific(),
        }
