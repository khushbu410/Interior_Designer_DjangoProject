from django.urls import path
from myapp import views
# from .views import login_view

urlpatterns = [
    
    path('',views.index,name='myapp'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('book//<service_name>/', views.Book_view, name='book'),
    path('meetdesigner/', views.meet_designer, name='meetdesigner')
    
    
]
