from django.contrib import admin
from .models import History


# Register your models here.
@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('userId', 'username', 'from_language', 'to_language', 'input_text', 'translation', 'query_time')
    ordering = ('userId',)
