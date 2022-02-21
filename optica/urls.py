"""optica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
import login.views as loginview
import cart.views as cartview

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('opticals.urls')),
    path('', include('home.urls')),
    path('product/', include('product.urls')),
    path('cart/', include('cart.urls')),
    path('', include('login.urls')),
    path('', include('register.urls')),
    path('', include('checkout.urls')),
    path('customadmin/', include('admin.urls')),
    path('logout',loginview.logoutUser, name='logout'),
    path('addCart/',cartview.addToCart, name="addCart"),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
