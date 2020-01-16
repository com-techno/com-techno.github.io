import datetime
import random
import string

from django.db import models
from django.utils import timezone


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class Game(models.Model):
    # game_tag = models.CharField('тег игры', max_length=5)

    game_tag = models.CharField('тэг игры', max_length=5, default=id_generator(5, string.ascii_uppercase + string.digits))
    game_name = models.CharField('название игры', max_length=50, default='Игра')
    game_present_cost_min = models.IntegerField('минимальная стоимость подарка', default=200)
    game_present_cost_max = models.IntegerField('максимальная стоимость подарка', default=1000)
    pub_date = models.DateField('дата начала игры', default=timezone.now)
    game_timer = models.IntegerField('длительность игры', default=5)

    def __str__(self):
        return self.game_tag

    def hasended(self):
        return self.pub_date < timezone.now() - datetime.timedelta(days=self.game_timer)

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'


class Gamer(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    gamer_name = models.CharField('имя игрока', max_length=20)

    def __str__(self):
        return self.gamer_name

    class Meta:
        verbose_name = 'Игроки'
        verbose_name_plural = 'Игрок'
