from django.contrib import admin
from accounts.models import User , Profile
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin) :
    model = User
    list_display = ['email','is_superuser','is_active','is_verified']
    list_filter = ['is_superuser','is_active','is_verified']
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
                'is_superuser','is_staff','is_active','is_verified'
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
            "fields" : ('email','password1','password2','is_superuser','is_staff','is_active','is_verified'),
        }),
    )


admin.site.register(Profile)
admin.site.register(User,CustomUserAdmin)