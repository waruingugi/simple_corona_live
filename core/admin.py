from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from core.models import Users, Choices


class AdminPage(UserAdmin):
    list_display = ('time_stamp', 'username')
    search_fields = ('username',)

    fieldsets = (
        ('Site Users', {'fields': ('username',
        )}),
        ('Permissions', {'fields': ('is_admin',)})
    )

    ordering = ('username',)
    list_filter = ('username',)

    filter_horizontal = ()


class ChoicesPage(admin.ModelAdmin):
    list_display = ('timestamp', 'user', 'answers', 'new_cases', 'active_cases', 'total_cases')
    search_fields = ('answers', 'new_cases', 'active_cases', 'total_cases')


admin.site.register(Users, AdminPage)
admin.site.unregister(Group)
admin.site.register(Choices, ChoicesPage)
