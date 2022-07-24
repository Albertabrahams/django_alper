from django.urls import path
from haberler.api import views as api_views

urlpatterns = [
    path('makaleler/', api_views.MakaleListCreateAPIView.as_view(), name='makale-list-create'),
    path('makaleler/<int:pk>/', api_views.MakaleDetailAPIView.as_view(), name='makale-detail'),
    path('yazarlar/', api_views.GazeteciListCreateAPIView.as_view(), name='yazar-list-create'),
]

#Function based views
# urlpatterns = [
#     path('makaleler/', api_views.makale_list_create_api_view, name='makale-listesi'),
#     path('makaleler/<int:pk>/', api_views.makale_detail_api_view, name='makale-detay'),
# ]