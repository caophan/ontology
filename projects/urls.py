from django.urls import path
from . import views

urlpatterns = [
    path("teachers", views.teacher_index, name="teacher_index"),
    path("teachers/search", views.teacher_search, name="teacher_search"),
    path("teachers/<str:id>", views.teacher_detail, name="teacher_detail"),
    path("products", views.product_index, name='product_index'),
    path("products/search", views.product_search, name="product_search"),
    path("products/<str:id>", views.product_detail, name='product_detail'),
    path("subjects", views.subject_index, name='subject_index'),
    path("subjects/<str:id>", views.subject_detail, name='subject_detail')
]
