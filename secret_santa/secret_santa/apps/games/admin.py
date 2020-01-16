from django.contrib import admin

from .models import Game, Gamer


admin.site.register(Gamer)
admin.site.register(Game)
