import hashlib
from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
from django.conf import settings

class SessionHijackingProtectionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Check if the user is authenticated
        if request.user.is_authenticated:
            session_key = request.session.session_key
            ip_address = request.META.get('REMOTE_ADDR')
            user_agent = request.META.get('HTTP_USER_AGENT')
            
            # Create a hash of IP address and User-Agent to compare across requests
            session_info_hash = hashlib.sha256(f"{ip_address}{user_agent}".encode('utf-8')).hexdigest()

            # If this hash is different from the one stored in the session, it means the session is compromised
            if 'session_info_hash' in request.session and request.session['session_info_hash'] != session_info_hash:
                logout(request)  # Log the user out
                return JsonResponse({'error': 'Session hijacking detected! Please log in again.'}, status=401)

            # Store the session info hash for future comparisons
            request.session['session_info_hash'] = session_info_hash

        return None  # Continue to the next middleware

