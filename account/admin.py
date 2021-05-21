from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account


class AccountAdmin(UserAdmin):
    list_display = (
    'email', 'username', 'firstname', 'lastname', 'date_joined', 'last_login', 'is_admin', 'is_staff', 'is_active')
    search_fields = ('email', 'username', 'firstname', 'lastname')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ('firstname', 'lastname', 'date_joined', 'last_login', 'is_admin', 'is_staff', 'is_active')
    fieldsets = ()

    actions = ['activate_accounts', 'deactivate_accounts', ]

    def activate_accounts(self, request, queryset):
        queryset.update(is_active=True)

    def deactivate_accounts(self, request, queryset):
        queryset.update(is_active=False)


admin.site.register(Account, AccountAdmin)
