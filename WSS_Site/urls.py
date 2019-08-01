from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from WSS_Site.error_handler_views import Handler404View

urlpatterns = [
                  url(r'^jet/', include('jet.urls', 'jet')),
                  url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
                  url(r'^captcha/', include('captcha.urls')),
                  url(r'^admin/', admin.site.urls),
                  url(r'^', include('WSS.urls', namespace='wss')),
                  url(r'^', include('events.urls', namespace='events')),
                  url(r'^', include('people.urls', namespace='people')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'WSS Administration'
admin.site.site_title = 'WSS Administration'

handler404 = Handler404View.as_view()
