from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('usuarios/', include('usuarios.urls')),

    path('sintomas/', include('sintomas.urls')),

    path('sinais-vitais/', include('sinais_vitais.urls')),

    path('medicamentos/', include('medicamentos.urls')),

    path('', include('dashboard.urls')),
]
