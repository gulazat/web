from django.urls import path

from . import views

app_name = 'my_data'


urlpatterns = [
    path('main/',views.main,name='data_main'),
    path('details/<int:pk>',views.data_detail,name='data_detail'),
    path('category/<int:pk>', views.category, name='data_category'),
    path('tag/<int:pk>', views.tag, name='data_tag'),

    path('search/',views.search,name = 'data_search'),
    path('all_tags/',views.all_tags,name = 'data_alltags'),
    path('all_categ/',views.all_categ,name = 'data_categ'),
    path('reply/<int:pk>',views.reply,name = 'comment_reply'),

]