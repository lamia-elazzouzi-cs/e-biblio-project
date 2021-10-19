"""
    e_biblio URL Configuration
"""
from django.contrib import admin
from django.urls import path
from e_biblio_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.welcome_fct),
    path('ouvrages', views.page_ouvrages),
    path('chercheurs', views.page_chercheurs),
    path('emprunts', views.page_emprunts),
    path('', views.login_admin),
    path('logout', views.logout_admin),
    path('newouvrage', views.new_ouvrage, name="newouvrage"),
    path('updateouvrage/<int:id>', views.update_ouvrage),
    path('destroyouvrage/<int:id>', views.destroy_ouvrage),
    path('newchercheur', views.new_chercheur, name="newchercheur"),
    path('updatechercheur/<int:id>', views.update_chercheur),
    path('destroychercheur/<int:id>', views.destroy_chercheur),
    path('newemprunt', views.new_emprunt, name="newemprunt"),
    path('updateemprunt/<int:id>', views.update_emprunt),
    path('destroyemprunt/<int:id>', views.destroy_emprunt),
]
