from django.contrib import admin
from .models import Firms, CarMarks, Cars


admin.site.register(CarMarks)
admin.site.register(Firms)
admin.site.register(Cars)
