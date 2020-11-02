from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.views.decorators.csrf import csrf_exempt

from admin_black.models import AdminBlackSetting


class CustomUserAdmin(UserAdmin):
    def get_urls(self):
        urls = [
                   path('admin_black-setting/', self.admin_site.admin_view(self.setting), name='admin_black_setting'),
               ] + super().get_urls()
        return urls

    @csrf_exempt
    def setting(self, request):
        user = request.user
        if request.method == 'POST':
            params = {}

            sidebar_background = request.POST.get('sidebar_background', None)
            if sidebar_background:
                params['sidebar_background'] = sidebar_background

            dark_mode = request.POST.get('dark_mode', None)
            if dark_mode:
                params['dark_mode'] = bool(int(dark_mode))

            AdminBlackSetting.objects.update_or_create(user=user, defaults=params)

        return JsonResponse({'valid': True})


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
