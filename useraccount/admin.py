from django.contrib import admin
from useraccount.models import UserAccount

class UserAccountAdmin(admin.ModelAdmin):
    list_display = (
        "image",
        "phone_number",
        "location",
        "email",
        "password",
        # "confirm_password",
    )

admin.site.register(UserAccount, UserAccountAdmin)



