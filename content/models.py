from django.db import models


class Vacancy(models.Model):
    name = models.CharField(
        "Наименование",
        max_length=255,
    )
    responsibilities = models.TextField(
        "Обязанности",
        blank=True,
        null=True,
    )

    requirements = models.TextField(
        "Требования",
        blank=True,
        null=True,
    )

    salary = models.CharField(
        "Заработная плата",
        max_length=255,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"


class News(models.Model):
    img = models.ImageField(
        "Фото",
        upload_to="news",
        blank=True,
        null=True,
    )
    title = models.CharField(
        "Заголовок",
        max_length=255,
    )
    text = models.TextField(
        "Текст",
        blank=True,
        null=True,
    )

    tag = models.CharField(
        "Тэг",
        max_length=255,
        blank=True,
        null=True,
    )
    date = models.DateField(
        "Дата публикации",
        auto_now=False,
        auto_now_add=False,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class LicenseCategory(models.Model):
    name = models.CharField(
        "Название категории",
        max_length=255,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Категория лицензии"
        verbose_name_plural = "Категории лицензий"


class License(models.Model):
    img = models.ImageField("Фото", upload_to="licenses")
    category = models.ForeignKey(
        LicenseCategory,
        verbose_name="Категория",
        related_name="images",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Лицензия"
        verbose_name_plural = "Лицензии"
