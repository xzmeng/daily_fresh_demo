#!/user/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'df_order'

urlpatterns = [
    url(r'^$', views.order, name="order"),
    url(r'^push/$', views.order_handle, name="push"),
    path('order_again/<int:pk>', views.order_again, name="order-again"),
]