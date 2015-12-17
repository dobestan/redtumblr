from django.contrib import admin

from tumblr.models.blog import Blog


@admin.register(Blog)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display + (
        'slug',

        'created_at',
        'updated_at',
    )

    list_filter = admin.ModelAdmin.list_filter + (
        'is_blocked',
        'is_deleted',
    )

    inlines = (
    )

    search_fields = (
        'slug',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
    )
