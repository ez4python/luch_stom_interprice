from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from parler.admin import TranslatableAdmin

from apps.models import User, Category, Product


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email']

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )


@admin.register(Category)
class CategoryTranslatableAdmin(TranslatableAdmin):
    list_display = ['name']


@admin.register(Product)
class ProductTranslatableAdmin(TranslatableAdmin):
    list_display = ['title', 'price', 'quantity']
