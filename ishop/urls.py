from django.urls import path
from .import views 
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
   path('', views.index, name='home'),
   path('signup', views.signup, name='signup'),
   path('login', views.login, name='login'),
   path('logout', views.logout, name='logout'),
   path('cart', views.cart_details, name='cart'),
   path('about/', views.aboutUs, name='aboutUs'),
   path('contact/', views.contactUs, name='contactUs'),
   path('tracker/', views.tracker, name='trackingstatus'),
   path('search/', views.search, name='search'),
   path('productview/', views.productView, name='productView'),
   path('checkout/', views.checkout, name='checkout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)