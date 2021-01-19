from django.contrib import admin
from . import models
from django.contrib import messages
from django.utils.translation import ngettext


def make_published(modeladmin, request, queryset):
    updated=queryset.update(status='p')
    modeladmin.message_user(request, ngettext(
        '%d story was successfully marked as published.',
        '%d stories were successfully marked as published.',
        updated,
    ) % updated, messages.SUCCESS)


make_published.short_description = "Mark selected books as published"


def make_draft(modeladmin, request, queryset):
    updated=queryset.update(status='d')
    modeladmin.message_user(request, ngettext(
        '%d story was successfully marked as drafted.',
        '%d stories were successfully marked as drafted.',
        updated,
    ) % updated, messages.SUCCESS)


make_draft.short_description = "Mark selected books as draft"


@admin.register(models.Book)
class AdminBook(admin.ModelAdmin):
    list_display = ('name', 'pub_date', 'catToStr', 'status')
    actions = [make_published, make_draft]

    def catToStr(self, obj):
        return ','.join([category.catName for category in obj.category.active()])

    catToStr.short_description = 'category'


def make_active(modeladmin, request, queryset):
    updated=queryset.update(status='True')
    modeladmin.message_user(request, ngettext(
        '%d story was successfully marked as actived.',
        '%d stories were successfully marked as actived.',
        updated,
    ) % updated, messages.SUCCESS)


make_active.short_description = "Mark selected category as active"


def make_deactive(modeladmin, request, queryset):
    updated=queryset.update(status='False')
    modeladmin.message_user(request, ngettext(
        '%d story was successfully marked as deactived.',
        '%d stories were successfully marked as deactived.',
        updated,
    ) % updated, messages.SUCCESS)


make_deactive.short_description = "Mark selected category as deactive"


@admin.register(models.Category)
class CatAdmin(admin.ModelAdmin):
    list_display = ('catName', 'parent', 'status')
    actions = [make_deactive,make_active]