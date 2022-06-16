from django.urls import path

from .views import (
    Atom,
    Bez,
    Cam,
    Catalog,
    Company,
    Contact,
    Filtr,
    Index,
    News,
    Politic,
    Sos,
    Temp,
    Tran,
    Vacansii,
)

app_name = "content"

urlpatterns = [
    path("", Index.as_view()),
    path("atom/", Atom.as_view()),
    path("bez/", Bez.as_view()),
    path("cam/", Cam.as_view()),
    path("catalog/", Catalog.as_view()),
    path("company/", Company.as_view()),
    path("contact/", Contact.as_view()),
    path("filtr/", Filtr.as_view()),
    path("news/", News.as_view()),
    path("politic/", Politic.as_view()),
    path("sos/", Sos.as_view()),
    path("temp/", Temp.as_view()),
    path("tran/", Tran.as_view()),
    path("vacansii/", Vacansii.as_view()),
]
