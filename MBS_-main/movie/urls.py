from django.urls import path
from . import views

urlpatterns = [
    path('<int:movie_id>', views.detail, name='detail'),
    path('<int:movie_id>/create', views.createreview, name='createreview'),
    path('review/<int:review_id>', views.updatereview, name='updatereview'),
    path('review/<int:review_id>/delete', views.deletereview, name='deletereview'),
    path('movies/<int:movie_id>/purchase_tickets/', views.purchase_tickets, name='purchase_tickets'),
    path('movies/<int:movie_id>/purchase_confirm/', views.purchase_confirm, name='purchase_confirm'),
    path('movies/<int:movie_id>/purchase_complete/', views.purchase_complete, name='purchase_complete'),
]

