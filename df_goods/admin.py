from django.contrib import admin
from df_goods.models import *

class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ('gtitle','gprice','gunit','gclick','gstock','gcom')
    search_fields = ('gtitle',)

class AdvInfoAdmin(admin.ModelAdmin):
    list_display = ('apic','acom')

admin.site.register(TypeInfo)
admin.site.register(GoodsInfo,GoodsInfoAdmin)
admin.site.register(AdvInfo,AdvInfoAdmin)