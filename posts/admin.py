from django.contrib import admin

from posts.models import User,Post

admin.site.register(User)
admin.site.register(Post)
