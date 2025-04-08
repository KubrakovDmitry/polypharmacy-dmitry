from django.urls import path

from .views import *


urlpatterns = [
    path('addpage/', addpage_views, name='add_page'),
    path('addDrug/', addDrug_views, name='add_Drug'),
    path('addDrugGroup/', addDrugGroup_views, name='add_DrugGroup'),
    path('updateSideEffects/', updateSideEffects_views, name='update_SideEffects'),
]
