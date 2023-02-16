from django.contrib import admin
from .models  import *

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Album)
admin.site.register(Musician)
admin.site.register(Student)
admin.site.register(Module)