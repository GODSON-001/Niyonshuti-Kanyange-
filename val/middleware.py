# middleware.py
from django.utils import timezone
import logging
from django.core.cache import cache

logger = logging.getLogger('my_logger')

class UserActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Capture user activity
        logger.info(f"User {request.user} accessed {request.path} at {timezone.now()} from IP {request.META.get('REMOTE_ADDR')}")
        
        # Track user count
        user_count = cache.get('user_count', 0)
        user_count += 1
        cache.set('user_count', user_count)

        response = self.get_response(request)
        return response
