from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth.forms import UserChangeForm
from .models import Profile
from .forms import ProfileChangeForm, ProfileCreationForm

# Register your models here.
#admin.site.register(Profile, auth_admin.UserAdmin)
@admin.register(Profile)
class UserAdmin(auth_admin.UserAdmin):
    form = ProfileChangeForm
    add_form = ProfileCreationForm
    model = Profile
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Campos personalizados", {"fields": ("code","phone","profile_type","about",)}),
    )