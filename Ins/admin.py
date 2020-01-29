from django.contrib import admin
from Ins.models import (Post, InsUser, Like, UserConnection)

# Register your models here.

admin.site.register(Post)
admin.site.register(InsUser)
admin.site.register(Like)
admin.site.register(UserConnection)



