from django.contrib import admin
from .models import Aluna, Professora, Horario, Modalidade, Sala
# Register your models here.
admin.site.register(Aluna)
admin.site.register(Professora)
@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_filter = ('dia_da_semana', 'horario')
@admin.register(Modalidade)
class ModalidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sala')
    list_filter = ('sala',)
admin.site.register(Sala)
