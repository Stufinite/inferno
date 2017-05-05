
# -*- coding: utf-8 -*-
from django.conf.urls import url
from infernoWeb.view import gluttony
from infernoWeb.view import sloth
from infernoWeb.view import arrogant
urlpatterns = [
  url(r'^gluttony$',gluttony.index, name='gluttony'),#這樣做似乎是對應到,首頁
  url(r'^inside_resturant/$', gluttony.inside_resturant, name='inside_resturant'),
  url(r'^purchase/$', gluttony.purchase, name='purchase'),
  url(r'^check/$', gluttony.check, name='check'),
  url(r'^boss/$', gluttony.boss, name='boss'),
] + [
  # 課程心得的部份
  url(r'^sloth$',sloth.index, name='sloth'),
  url(r'^sloth/inside$',sloth.inside, name='slothInside'),
] + [
  # 求職網的部份
  url(r'^arrogant$',arrogant.index, name='arrogant'),
  url(r'^arrogant/inside$',arrogant.inside, name='arrogantInside')
]

