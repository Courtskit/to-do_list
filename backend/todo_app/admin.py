from django.contrib import admin
from todo_app.models import *

admin.site.register(List, ListItem)