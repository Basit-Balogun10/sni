from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account, Profile, WriterProfile


class AccountAdmin(UserAdmin):
    list_display = (
    'email', 'username', 'firstname', 'lastname', 'date_joined', 'last_login', 'is_admin', 'is_staff', 'is_active', 'is_writer')
    search_fields = ('email', 'username', 'firstname', 'lastname')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ('firstname', 'lastname', 'date_joined', 'last_login', 'is_admin', 'is_staff', 'is_active', 'is_writer', 'about')
    fieldsets = ()

    actions = ['activate_accounts', 'deactivate_accounts', ]

    def activate_accounts(self, request, queryset):
        queryset.update(is_active=True)

    def deactivate_accounts(self, request, queryset):
        queryset.update(is_active=False)


admin.site.register(Account, AccountAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'email_confirmed')
    search_fields = ('user', 'email_confirmed')
    readonly_fields = ('user', 'email_confirmed')

    list_filter = ('user', 'email_confirmed')
    filter_horizontal = ()
    ordering = ('user', 'email_confirmed')


admin.site.register(Profile, ProfileAdmin)

class WriterProfileAdmin(admin.ModelAdmin):
    list_display = ('user', )
    search_fields = ('user', )
    readonly_fields = ('user', )

    list_filter = ('user', )
    filter_horizontal = ()
    ordering = ('user', )


admin.site.register(WriterProfile, WriterProfileAdmin)