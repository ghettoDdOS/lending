from django.views.generic import ListView, TemplateView, DetailView

from .models import LicenseCategory
from .models import News as NewsModel
from .models import Vacancy


class Index(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["news"] = NewsModel.objects.all()
        return context


class Atom(TemplateView):
    template_name = "atom.html"


class Bez(TemplateView):
    template_name = "bez.html"


class Cam(TemplateView):
    template_name = "cam.html"


class Catalog(TemplateView):
    template_name = "catalog.html"


class Company(ListView):
    model = LicenseCategory
    template_name = "company.html"


class Contact(TemplateView):
    template_name = "contact.html"


class Filtr(TemplateView):
    template_name = "filtr.html"


class News(ListView):
    model = NewsModel
    template_name = "news.html"


class NewsDetail(DetailView):
    model = NewsModel
    template_name = "news-detail.html"


class Politic(TemplateView):
    template_name = "politic.html"


class Sos(TemplateView):
    template_name = "sos.html"


class Temp(TemplateView):
    template_name = "temp.html"


class Tran(TemplateView):
    template_name = "tran.html"


class Vacansii(ListView):
    model = Vacancy
    template_name = "vacansii.html"
