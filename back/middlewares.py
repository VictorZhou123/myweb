from django.shortcuts import redirect
from django.urls import reverse

class LoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if request.path.startswith('/back') and request.path not in ['/back/auth/login/','/back/auth/reg/','/back/auth/logout/']:
            if  not request.session.get('user',False):
                return redirect(reverse('back:login'))
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response