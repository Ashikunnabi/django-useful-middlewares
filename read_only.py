import json
from django.http import HttpResponseForbidden


def view_only_middleware(get_response):
    """ Only Get request allowd """

    def middleware(request):
        if request.method not in ['GET']:
            json_object = {0: 'Unauthorized operation'}
            return HttpResponseForbidden(json.dumps(json_object), content_type="application/json")
        return get_response(request)

    return middleware
