from django.db import models
from django.contrib.auth.models import User


class SecurityBranchReport(models.Model):
    # Филиалы
    class Branch(models.TextChoices):
        VLADIMIR = '01_ВПФ', 'Владимирский'
        KIROV = '02_КРФ', 'Кировский'
        KOMI = '03_КОФ', 'Коми'
        MARIEL = '04_МЧФ', 'Марий Эл и Чувашии'
        MORDOVIA = '05_МРФ', 'Мордовский'
        NIZHNIY = '06_НГФ', 'Нижегородский'
        ORENBUG = '07_ОРФ', 'Оренбургский'
        PERM = '08_ПМФ', 'Пермский'
        SAMARA = '09_СМФ', 'Самара'
        SARATOV = '10_СРФ', 'Саратовский'
        EKAT = '11_СВФ', 'Свердловский'
        UDMURTIA = '12_УДФ', 'Удмуртский'
        ULIANOVSK = '13_УЛФ', 'Ульяновский'
        PENZA = '14_ПНФ', 'Пензенский'

    # user
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    # Филиал
    branch = models.CharField(max_length=6,
                              choices=Branch.choices)
    # Не закрытие постов охраны
    field1 = models.IntegerField(default=0)
    # Отсутствие спец.средств и оружия
    field2 = models.IntegerField(default=0)
    # Ненадлежащее проведение досмотра
    field3 = models.IntegerField(default=0)
    # Самовольное покидание поста
    field4 = models.IntegerField(default=0)
    # Допущение проникновения посторонних лиц
    field5 = models.IntegerField(default=0)
    # Допущение прохода по чужому пропуску(без пропуска)
    field6 = models.IntegerField(default=0)
    # Нахождение на посту в нетрезвом виде
    field7 = models.IntegerField(default=0)
    # Неприбытие ГБР
    field8 = models.IntegerField(default=0)
    # Иные значимые нарушения
    field9 = models.IntegerField(default=0)
    # Создано
    created = models.DateTimeField(auto_now_add=True)
    # Обновлено
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.branch} {self.updated} {self.author}'