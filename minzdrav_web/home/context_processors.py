from __future__ import annotations

from wagtail.models import Site

from .models import ArticleIndexPage


def global_nav(request):
    site = Site.find_for_request(request)
    home_url = site.root_page.url if site else "/"

    articles_url = "#"
    if site:
        articles_index = (
            site.root_page.get_descendants(inclusive=True)
            .type(ArticleIndexPage)
            .live()
            .public()
            .first()
        )
        if articles_index:
            articles_url = articles_index.url

    return {
        "nav_home_url": home_url,
        "nav_articles_url": articles_url,
    }
