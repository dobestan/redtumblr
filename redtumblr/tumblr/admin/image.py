from django.contrib import admin

from tumblr.models.image import Image


@admin.register(Image)
class ImageModelAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display + (
        'original_url',

        'created_at',
        'updated_at',
    )

    list_filter = admin.ModelAdmin.list_filter + (
    )

    inlines = (
    )

    search_fields = (
    )

    readonly_fields = (
        'created_at',
        'updated_at',
    )
