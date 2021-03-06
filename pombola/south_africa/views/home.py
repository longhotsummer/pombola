from info.models import (
    InfoPage, Category as BlogCategory, Tag as BlogTag
)

from pombola.core.views import HomeView


class SAHomeView(HomeView):

    def get_context_data(self, **kwargs):
        context = super(SAHomeView, self).get_context_data(**kwargs)

        articles = InfoPage.objects.filter(
            kind=InfoPage.KIND_BLOG).order_by("-publication_date")

        articles_for_front_page = \
            InfoPage.objects.filter(
                categories__slug__in=(
                    'week-parliament',
                    'impressions'
                )
            ).order_by('-publication_date')

        context['news_articles'] = articles_for_front_page[:2]

        try:
            c = BlogCategory.objects.get(slug='mp-corner')
            context['mp_corner'] = articles.filter(categories=c)[0]
        except (BlogCategory.DoesNotExist, IndexError):
            context['mp_corner'] = None

        try:
            context['infographics'] = BlogTag.objects.get(name='infographic'). \
                entries.order_by('-created')[0:4]
        except BlogTag.DoesNotExist:
            context['infographics'] = []

        return context
