from django.contrib import admin
from .models import Aluna, Professora, Horario, Modalidade, Sala
# Register your models here.
admin.site.register(Aluna)
admin.site.register(Professora)
admin.site.register(Horario)
admin.site.register(Modalidade)
admin.site.register(Sala)
