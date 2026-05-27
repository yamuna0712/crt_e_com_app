from django.urls import path

from .views import add_product, view_all_products, del_by_id, add_to_cart,delete_cart_item,upd_by_id


urlpatterns = [
    path('add_product/',add_product),
    path('view_all_products/',view_all_products),
    path('del_by_id/<int:id>/',del_by_id),
    path('add_to_cart/',add_to_cart),
    path('delete_cart_item/<int:id>/', delete_cart_item),
path('upd_by_id/<int:id>/', upd_by_id),
]