from django.contrib import admin
from .models import MemorandumModel


@admin.register(MemorandumModel)
class MemorandumAdmin(admin.ModelAdmin):
    list_display = ['email', 'send_date', 'created']
    readonly_fields = ['name', 'email', 'send_date', 'created']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields
        return []

    def get_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields
        else:
            return self.readonly_fields + ['text']

    def get_fieldsets(self, request, obj=None):
        if obj:
            return [(None, {'fields': self.readonly_fields}), ]
        else:
            return [(None, {'fields': ['name', 'email', 'send_date', 'text']}), ]