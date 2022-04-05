from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from rooms import models as room_models

# Register your models here.


# User 안에 Room을 불러와서 설정할 수 있는 코드
# 불필요 한것 같아서 제외
# class RoomInline(admin.TabularInline):
#     model = room_models.Room


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""

    # Room class를 정의한 후 불러오기 위한 코드, 불필요해서 제외
    # inlines = (RoomInline,)

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custum Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birstdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

    list_filter = UserAdmin.list_filter + ("superhost",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
        "is_active",
    )
