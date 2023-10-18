from django.db import models
from django.contrib.auth.models import AbstractUser
from .utilities import get_timestamp_path


class AdvUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True,
                                       verbose_name='Прошел активацию?')
    send_messages = models.BooleanField(default=True,
                                        verbose_name='Оповещать при новых комментариях?')

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.fk_set = None

    def delete(self, *args, **kwargs):
        for fk in self.fk_set.all():
            fk.delete()
        super().delete(*args, **kwargs)

    class Meta(AbstractUser.Meta):
        pass


class Query(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=500, help_text="Описание")
    image = models.ImageField(blank=True, upload_to=get_timestamp_path, verbose_name='Изображение')

    # LOAN_STATUS = (
    #     ('m', 'В обработке'),
    #     ('o', 'Принято в работу'),
    #     ('a', 'Выполнено'),
    # )
    #
    # status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Статус заявки')

    LOAN_CATEGORY = (
        ('m', '3D-дизайн'),
        ('o', '2D-дизайн'),
        ('a', 'Эскиз'),
    )

    category = models.CharField(max_length=1, choices=LOAN_CATEGORY, blank=True, help_text='Категория')

    def delete(self, *args, **kwargs):
        for ai in self.additionalimage_set.all():
            ai.delete()
        super().delete(*args, **kwargs)


class AdditionalImage(models.Model):
    fk = models.ForeignKey(Query, on_delete=models.CASCADE, verbose_name='Заявка')
    image = models.ImageField(upload_to=get_timestamp_path, verbose_name='Изображение')
