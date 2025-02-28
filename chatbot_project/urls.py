from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chatbot_app.urls')),
    path('', RedirectView.as_view(url='/chat/', permanent=False)),

    # path('api/', include('chatbot_api.urls')),               # API endpoints for frontend/ML clients
    # path('accounts/', include('django.contrib.auth.urls')),  # Login/logout if you add auth
]
