from django.core.exceptions import PermissionDenied


blacklisted_ips = ['192.168.1.1', '192.168.1.2']


class BlockIpMiddleware:
    """ Block blacklisted ip address """

    def _init_(self, get_response):
        self.get_response = get_response

    def _call_(self, request):
        # get ip
        ip = request.META.get('REMOTE_ADDR')
        
        if ip in blacklisted_ips:
            raise PermissionDenied

        response = self.get_response(request)

        # Code that is executed in each request after the view is called

        return response
