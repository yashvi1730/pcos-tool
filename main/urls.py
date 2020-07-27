from django.urls import path
from main import views

urlpatterns=[
    path('homepage',views.form_view,name="homepage"),
    path('medical_history',views.medical_history_form,name="medical_history"),
    path('schedule',views.schedule_form,name="schedule"),
    path('pcos_history',views.pcos_history_form,name="pcos_history"),
    path('purpose',views.purpose_form,name="purpose"),
    path('test',views.test,name="test"),
    path('mensis',views.mensis,name="mensis"),
    path('lastpage',views.lastpage,name="lastpage"),
   
]