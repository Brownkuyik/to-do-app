# The middleware here is executed before any of the views to check for what you dont intent to happen on your site
from django.core.cache import cache
from django.http import HttpResponseForbidden
from django.conf import settings



class CrawlerLockerMiddleware(object):
    def __init__(self, get_response=None): #this should not take more than this values or variables
        self.get_response = get_response

    
    def __call__(self, request):
        # TO GET THE IP ADDRESS OF USERS
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        ip = x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')

        # UNIQUE KEY FOR THE ADDRESS
        ip_cache_key = "django_bot_crawler_blocker:ip_rate" + ip
        

        ip_hit_timeout = settings.IP_HITS_TIMEOUT if hasattr(settings, 'IP_HITS_TIMEOUT') else 60
        max_allowed_hits = settings.MAX_ALLOWED_HITS_PER_IP if hasattr(settings, "MAX_ALLOWED_HITS_PER_IP") else 2000

        # get the hits by this IP in last IP_TIMEOUT time
        this_ip_hits = cache.get(ip_cache_key)

        if not this_ip_hits:
            this_ip_hits = 1;
            cache.set(ip_cache_key, this_ip_hits, ip_hit_timeout)
        else:
            this_ip_hits +=1
            cache.set(ip_cache_key, this_ip_hits)

        if this_ip_hits>max_allowed_hits:
            # return HttpResponseForbidden()
            return render(request, "ImageApp/access_denials.html", status = 400)
        else:
            response = self.get_response(request)
            return response

# if dont want someone to used any other device like phone to access your side. used below code
# first import user_agents 

import logging
from django.http import HttpResponse
import user_agents



logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()



class CountResponseMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        self.count_requests = 0
        self.count_exceptions = 0

    def __call__(self, request, *args, **kwargs):
        self.count_requests +=1
        logger.info(f'Handled {self.count_requests} request so far')
        return self.get_response(request)

    def process_exceptions(self, request, exceptions):
        self.count_exceptions +=1
        logger.error(f"Encountered {self.count_exceptions} exceptions so far")

class SetUserAgentMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwds):
        request.user_agents = user_agents.parse(request.META["HTTP_USER_AGENT"])
        return self.get_response(request)


from django.shortcuts import render, redirect

class BlockMobileMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response


    
    def __call__(self, request, *args, **kwargs):
        # print(request.user_agents)
        if request.user_agents.is_mobile:
            return HttpResponse("Mobile device not allowed here", status = 400)
            # return render(request, "ImageApp/not.html", status=400) this is used to create a new html file for the block devices to display the message
        return self.get_response(request)




