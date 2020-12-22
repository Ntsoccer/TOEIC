from django.urls import path, include
from . import views

app_name = 'toeicapp'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('post_create', views.PostCreate.as_view(), name='post_create'),
    path('post_detail/<int:pk>', views.PostDetail.as_view(), name='post_detail'),
    path('post_update/<int:pk>', views.PostUpdate.as_view(), name='post_update'),
    path('post_delete/<int:pk>', views.PostDelete.as_view(), name='post_delete'),
    path('post_list', views.PostList.as_view(), name='post_list'),
    path('privacy', views.Privacy.as_view(), name='privacy'),
    path('service', views.Service.as_view(), name='service'),
    path('asked_question/', views.AskedQuestion.as_view(), name='asked_question'),
    path('login', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('user_create/', views.UserCreate.as_view(), name='user_create'),
    path('user_create/done/', views.UserCreateDone.as_view(),
         name='user_create_done'),
    path('user_create/complete/<token>/',
         views.UserCreateComplete.as_view(), name='user_create_complete'),
    path('user_detail/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('user_update/<int:pk>/', views.UserUpdate.as_view(), name='user_update'),
    path('password_change/', views.PasswordChange.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDone.as_view(),
         name='password_change_done'),
    path('password_reset/', views.PasswordReset.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDone.as_view(),
         name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/',
         views.PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', views.PasswordResetComplete.as_view(),
         name='password_reset_complete'),
    path('contact_form', views.ContactFormView.as_view(), name='contact_form'),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('category_list', views.CategoryList.as_view(), name='category_list'),
    path('category_detail/<str:name_en>',
         views.CategoryDetail.as_view(), name='category_detail'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
