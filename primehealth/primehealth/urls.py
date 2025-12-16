from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),

    path('', include('dashboard.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('sintomas/', include('sintomas.urls')),
    path('sinais-vitais/', include('sinais_vitais.urls')),
    path('medicamentos/', include('medicamentos.urls')),
]
