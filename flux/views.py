from django.views.generic.base import TemplateView

class HomePageView(TemplateView):

    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

class AboutUs(TemplateView):

    template_name = "aboutus.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class News(TemplateView):

    template_name = "news.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
        

