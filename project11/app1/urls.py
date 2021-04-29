from django.urls import path
from .views import *


app_name= 'app1'

urlpatterns = [
    path('', CustomerListView.as_view(),name='customer-list-view'),
    path('', render_pdf_view,name='test-view'),
    path('pdf/<pk>/', customer_pdf_view,name='customer-pdf-view'),
]