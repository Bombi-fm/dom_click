from django.contrib import admin
from .models import Client, ApplicationType, Application, ApplicationWTypes, ApplicationStatus
from rangefilter.filters import DateRangeFilter

# Register your models here.

class ApplicationTypeInLine(admin.TabularInline):
    model = ApplicationWTypes
    extra = 0
    can_delete = False


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    search_fields = ('last_name', 'id')


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['pub_date', 'client', 'status']
    list_filter = [('pub_date', DateRangeFilter), 'status', 'type']
    search_fields = ('pub_date',)

    inlines = (ApplicationTypeInLine,)


@admin.register(ApplicationType)
class ApplicationTypeAdmin(admin.ModelAdmin):
    search_fields = ('name', 'id')


@admin.register(ApplicationStatus)
class ApplicationStatusAdmin(admin.ModelAdmin):
    search_fields = ('name', 'id')
