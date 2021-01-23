"""
Middleware to log all requests and responses.
Uses a logger configured by the name of YOUR_LOGGER
to log all requests and responses according to configuration
specified for YOUR_LOGGER.
"""
import logging
import time


logger = logging.getLogger('activity_logger')


class RequestLogMiddleware:
    """ Request Logging Middleware. """

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        """Set Request Start Time to measure time taken to service request."""
        request.start_time = time.time()

        response = self.get_response(request)

        log_data = self.extract_log_info(request=request, response=response)
        logger.info(log_data)

        return response

    def process_exception(self, request, exception):
        """Log Exceptions."""
        log_data = self.extract_log_info(request, exception)
        logger.info(log_data)
        return exception

    @staticmethod
    def extract_log_info(request, response=None):
        """Extract appropriate log info from requests/responses/exceptions."""

        log_data = {
            'remote_address': request.META.get('REMOTE_ADDR'),
            'request_method': request.method,
            'request_path': request.get_full_path(),
            'run_time': time.time() - request.start_time,
            'request_body': str(request.body, 'utf-8'),
            'response_body': response.content
        }
        return log_data

