from django.contrib import admin
from .models import *

admin.site.register(Records)
admin.site.register(Orders)

admin.site.site_header = 'CarServise'

