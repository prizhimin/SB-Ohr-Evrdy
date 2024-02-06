from django.contrib import admin
from .models import SecurityBranchReport


@admin.register(SecurityBranchReport)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['author', 'branch', 'created', 'updated']
    list_filter = ['branch', 'created', 'updated', 'author']
    # search_fields = ['branch', 'created', 'updated', 'author']
    ordering = ['branch', 'updated']

