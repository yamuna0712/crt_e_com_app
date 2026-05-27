from django.urls import path
from .views import add_book, get_books, home_page, file2, profile_page,contact_page,portfolio_home,portfolio_contact,grade,add_user

urlpatterns = [
    path('add/', add_book),
    path('get/',get_books),
    path('home_page',home_page),
    path('file2',file2),
    path('profile_page',profile_page),
    path('contact_page',contact_page),
    path('port_home',portfolio_home),
    path('port_contact',portfolio_contact),
    path('<int:marks>',grade),
    path('user_form',add_user),

]