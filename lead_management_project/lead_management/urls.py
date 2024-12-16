# from django.urls import path
# from . import views

# urlpatterns = [
#     path('login/', views.login_view, name='login'),
#     path('signup/', views.signup, name='signup'),
#     path('logout/', views.logout_view, name='logout'),
#     path('dashboard/', views.dashboard, name='dashboard'),
#     path('leads/', views.lead_list, name='leads'),
#     path('add_lead/', views.add_lead, name='add_lead'),
#     path('edit_lead/<int:pk>/', views.edit_lead, name='edit_lead'),
#     path('delete_lead/<int:pk>/', views.delete_lead, name='delete_lead'),
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('accounts/login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('leads/', views.lead_list, name='leads'),
    path('contacts/', views.contact_list, name='contacts'),
    path('contacts/add/', views.add_contact, name='add_contact'),
    path('contacts/edit/<int:pk>/', views.edit_contact, name='edit_contact'),
    path('contacts/delete/<int:pk>/', views.delete_contact, name='delete_contact'),
    path('add_lead/', views.add_lead, name='add_lead'),
    path('edit_lead/<int:pk>/', views.edit_lead, name='edit_lead'),
    path('delete_lead/<int:pk>/', views.delete_lead, name='delete_lead'),
    # path('sales_pipeline/', views.sales_pipeline, name='sales_pipeline'),
    # path('add_sales_pipeline/', views.add_sales_pipeline, name='add_sales_pipeline'),
    # path('update_stage/<int:pk>/', views.update_stage, name='update_stage'),
    
    path('sales_pipeline/', views.sales_pipeline, name='sales_pipeline'),
    path('sales_pipeline/add/', views.add_sales_pipeline, name='add_sales_pipeline'),
    path('sales_pipeline/update/<int:pk>/', views.update_stage, name='update_stage'),
    path('sales_pipeline/lead_progress/<int:pk>/', views.view_lead_progress, name='view_lead_progress'),
    path('report_and_analytics/', views.report_and_analytics, name='report_and_analytics'),
    
    path('', views.login_view, name='login'),  # Default to login page if the root URL is accessed

]

from django.urls import include

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),  # Use the default authentication URLs
]
