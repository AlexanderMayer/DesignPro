from django.contrib import admin
from .models import AdvUser
from .models import Query, AdditionalImage


class AdditionalImageInline(admin.TabularInline):
    model = AdditionalImage


class QueryAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary', 'category', 'image')
    fields = ('title', 'summary', 'category', 'image', 'is_active')
    inlines = (AdditionalImageInline,)


admin.site.register(Query, QueryAdmin)
admin.site.register(AdvUser)
