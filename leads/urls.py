from django.urls import path

from .views import (
    lead_list, lead_details, lead_create, lead_update, lead_delete,
    LeadListView, LeadDetailView, LeadCreateView, LeadUpdateView, LeadDeleteView,
    CategoryListView, CategoryDetailView
)
app_name="leads"

urlpatterns = [
    path('', LeadListView.as_view(), name="home_page"),
    path('<int:pk>/', LeadDetailView.as_view(), name="lead_details"),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name="lead_update"),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name="lead_delete"),
    path('create/', LeadCreateView.as_view(), name="lead_create"),
    path('categories/', CategoryListView.as_view(), name="category-list"),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name="category-detail"),
]