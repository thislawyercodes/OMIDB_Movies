from django.core.wsgi import get_wsgi_application
import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "IMDBMovies.settings")
application = get_wsgi_application()
app = application


def vc_handler(request, context):
    return app(request, context)



