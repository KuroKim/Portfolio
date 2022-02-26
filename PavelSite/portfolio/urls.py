from django.urls import path

from .views import *


urlpatterns = [
    path('', PortfolioHome.as_view(), name='home'),
    # path('addpage/', AddPage.as_view(), name='add_page'),

]

