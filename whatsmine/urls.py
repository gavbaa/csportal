from django.urls import path

from . import views

urlpatterns = [
    path('product/<int:product_id>', views.my_releases_for_product, name='product_view'),
    path('product/<int:product_id>/release/<int:release_id>', views.release, name='release_view'),
    path('product/<int:product_id>/release/<int:release_id>/download/<int:release_file_id>', views.release_download,
         name='release_download'),
]
