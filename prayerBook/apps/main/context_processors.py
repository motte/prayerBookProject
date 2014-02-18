from django.conf import settings


def project_settings(request):
    return {
        'PARSE_API_KEY': settings.PARSE_API_KEY,
        'PARSE_JS_KEY': settings.PARSE_JS_KEY,
    }


def parse_auth(request):
    authenticated = 'parse_session_token' in request.session
    return {'PARSE_AUTHENTICATED': authenticated}