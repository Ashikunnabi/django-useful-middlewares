from django.http import HttpResponse


class BlockMobileMiddleware:
    """ Restrict to view application from mobile devices. """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        if request.user_agent.is_mobile:
            return HttpResponse("Mobile devices are not supported", status=400)
        return self.get_response(request)
