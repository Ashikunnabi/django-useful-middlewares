from path.of.your.app import models


def RequestExposerMiddleware(get_response):
    """ Pass request object to specific model.
        
        By default, Django models have not accessed to request object. That is why we are unable to work with currently logged in user's information in models.py. This middleware will help to expose the request object to a specific model.
    """

    def middleware(request):
        # you can access the request object using, exposed_request
        models.exposed_request = request
        response = get_response(request)
        return response

    return middleware
