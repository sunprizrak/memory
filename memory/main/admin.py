from django.contrib import admin
from .models import PostalLetterModel


@admin.register(PostalLetterModel)
class MemorandumAdmin(admin.ModelAdmin):
    list_display = ['user', 'name_from', 'email', 'send_date', 'name_to', 'address', 'created']
    readonly_fields = ['name_from', 'email', 'send_date', 'name_to', 'address', 'created']

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
            return [(None, {'fields': ['user', 'name_from', 'email', 'send_date', 'name_to', 'address',  'text']}), ]