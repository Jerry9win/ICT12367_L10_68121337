from django.urls import path
from myapp import views

urlpatterns = [
    # หน้าแรก (Root)
    path('', views.index, name='index'),

    # หน้าเกี่ยวกับเรา (แนะนำให้ใส่ / ปิดท้ายเพื่อให้เป็นมาตรฐานเดียวกัน)
    path('about/', views.about, name='about'),

    # หน้าแบบฟอร์ม
    path('form/', views.form, name='form'),
]