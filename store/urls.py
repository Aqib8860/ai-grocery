from django.urls import path
from store.views import *


app_name = 'store'

urlpatterns = [
    path('add-item', AddItemView.as_view(), name='add-item'),
    path('update-item/<str:item_id>', UpdateItemView.as_view(), name='update-item'),
    path('delete-item/<str:item_id>', DeleteItemView.as_view(), name='delete-item'),
    path('today-items', TodayItemsView.as_view(), name='today-items'),

]
