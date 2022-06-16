from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = "index.html"


class Atom(TemplateView):
    template_name = "atom.html"


class Bez(TemplateView):
    template_name = "bez.html"


class Cam(TemplateView):
    template_name = "cam.html"


class Catalog(TemplateView):
    template_name = "catalog.html"


class Company(TemplateView):
    template_name = "company.html"


class Contact(TemplateView):
    template_name = "contact.html"


class Filtr(TemplateView):
    template_name = "filtr.html"


class News(TemplateView):
    template_name = "news.html"


class Politic(TemplateView):
    template_name = "politic.html"


class Sos(TemplateView):
    template_name = "sos.html"


class Temp(TemplateView):
    template_name = "temp.html"


class Tran(TemplateView):
    template_name = "tran.html"


class Vacansii(TemplateView):
    template_name = "vacansii.html"
