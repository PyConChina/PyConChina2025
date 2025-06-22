from django.conf import settings
from django.utils import translation


class LocaleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 判断请求路径是否以 /prefix/ 开头
        if request.path.startswith(f"{settings.URL_PREFIX}en/"):
            translation.activate("en")
        else:
            translation.activate(settings.LANGUAGE_CODE)

        response = self.get_response(request)
        return response
