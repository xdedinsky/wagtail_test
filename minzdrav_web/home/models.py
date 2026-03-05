from django.db import models

from wagtail.admin.panels import FieldPanel
from wagtail.models import Page
from wagtail.fields import RichTextField


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]


class ArticleIndexPage(Page):
    subpage_types = ["home.ArticlePage"]

    def get_context(self, request):
        context = super().get_context(request)
        context["articles"] = (
            self.get_children().live().order_by("-first_published_at")
        )
        return context


class ArticlePage(Page):
    publication_date = models.DateField("Publication date")
    content = RichTextField()
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content_panels = Page.content_panels + [
        FieldPanel("publication_date"),
        FieldPanel("content"),
        FieldPanel("image"),
    ]