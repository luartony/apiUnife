from django.conf.urls import url, include
from rest_framework import routers
from apiAlumnas import views
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'Ejemplos', views.EjemploViewSet)
router.register(r'MariaAlegre', views.MariaAlegreViewSet)
router.register(r'EdyAstete', views.EdyAsteteViewSet)
router.register(r'JeseniaFranco', views.JeseniaFrancoViewSet)
router.register(r'JenniferGonzales', views.JenniferGonzalesViewSet)
router.register(r'YaquelinHerrera', views.YaquelinHerreraViewSet)
router.register(r'MilagrosMagallanes', views.MilagrosMagallanesViewSet)
router.register(r'VanessaPerez', views.VanessaPerezViewSet)
router.register(r'YaniraPeña', views.YaniraPeñaViewSet)
router.register(r'LadiVega', views.LadiVegaViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 