from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.serializerview)


admin.site.site_header = "E_Shop Admin"
admin.site.site_title = "E_Shop Admin Portal"
admin.site.index_title = "Welcome to E_Shop Portal"

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('signin', views.SignIn, name="signup"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('cart', views.cart_info, name="cart"),
    path('checkout', views.checkout, name="checkout"),
    path('order', views.ordr_info, name="order"),
    path('buynow', views.buy, name="buy"),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
