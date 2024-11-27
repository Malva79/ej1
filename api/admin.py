from django.contrib import admin
# modelo programador importado desde MODELS (se creara solo con DRF)
from .models import programmer

# Register your models here.
# con este registro hacemos visible el modelo en panel de administracion.
admin.site.register(programmer)
