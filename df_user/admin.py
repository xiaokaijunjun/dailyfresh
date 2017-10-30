from django.contrib import admin
from df_user.models import *
# Register your models here.

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('uname','upwd','uemail','ushou','uphone')


admin.site.register(UserInfo,UserInfoAdmin)