from django.contrib import admin
from accounts.models import User
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin) :
    model = User
    list_display = ['email','is_superuser','is_active']
    list_filter = ['is_superuser','is_active']
    search_fields = ['email','is_superuser','is_active']
    ordering = ('email',)

    fieldsets = (
        ('Authentication',{
            "fields" : (
                'email','password'
            ),
        }),
        ('Permissions',{
            "fields" : (
                'is_superuser','is_staff','is_active'
            ),
        }),
        ('Group Permissions',{
            "fields" :(
                'groups','user_permissions'
            ),
        }),
        ('important date',{
            "fields" : (
                'last_login',
            ),
        })
    )

    # for add user
    add_fieldsets = (
        (None,{
            "classes":("wide"),
            "fields" : ('email','password1','password2','is_superuser','is_staff','is_active'),
        }),
    )


admin.site.register(User,CustomUserAdmin)