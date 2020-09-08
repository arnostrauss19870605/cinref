from django.urls import path

from . import views
from .views import ReferralCreateView, ReferralDetailView, ReferralListView,ReferredCreateView

urlpatterns = [
    path('referrals/', views.Referral.as_view()),
    path('referrals/<str:referral_id>/', views.ReferralDetail.as_view()),
    path('referrals/<str:referral_id>/referred/', views.Referred.as_view()),
    path('referrals/<str:referral_id>/referred/<str:referred_id>/', views.ReferredDetail.as_view()),
    path('referral/new/', ReferralCreateView.as_view(), name='referral_new'),
    path('referral/detail/<str:pk>/', ReferralDetailView.as_view(), name='referral_detail'),
    path('referral/home/', ReferralListView.as_view(), name='home'),
    path('referred/new/<str:pk>/', ReferredCreateView.as_view(), name='referred_new'),
    path('referral/done', views.index, name='index'),
]
