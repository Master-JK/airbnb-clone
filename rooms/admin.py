from csv import list_dialects
from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models

# Register your models here.


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()


class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """Room Admin Definition"""

    inlines = (PhotoInline,)

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "name",
                    "description",
                    "country",
                    "city",
                    "adress",
                    "price",
                    "room_type",
                ),
            },
        ),
        (
            "Times",
            {
                "fields": ("check_in", "check_out", "instant_book"),
            },
        ),
        (
            "More About The Space",
            {
                "classes": ("collapse",),
                "fields": ("guests", "beds", "bedrooms", "baths"),
            },
        ),
        (
            "Spaces",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "houserules"),
            },
        ),
        (
            "Last Details",
            {
                "fields": ("host",),
            },
        ),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    ordering = ("name", "price")

    list_filter = (
        "instant_book",
        "city",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "houserules",
        "country",
    )

    raw_id_fields = ("host",)

    search_fields = ("=city", "^host__username")

    filter_horizontal = (
        "amenities",
        "facilities",
        "houserules",
    )

    def count_amenities(self, obj):  # obj is current row(room)
        return obj.amenities.count()

    count_amenities.short_description = "Count Amenities"

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Count Photos"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """Photo Admin Definition"""

    list_display = (
        "__str__",
        "get_thumbnail",
    )

    def get_thumbnail(self, obj):

        return mark_safe(f"<img width=50px src={obj.file.url} />")

    get_thumbnail.short_description = "Thumbnail"
