from django.contrib import admin

from .models import License, LicenseCategory, News, Vacancy

admin.site.register(Vacancy)
admin.site.register(News)


class LicenseImagesInline(admin.TabularInline):
    model = License


@admin.register(LicenseCategory)
class LicenseAdmin(admin.ModelAdmin):
    inlines = [LicenseImagesInline]
