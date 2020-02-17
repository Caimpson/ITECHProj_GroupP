from django.urls import path
from choonz import views
from choonz.views import AboutView, AddPlaylistView, IndexView, AddPageView, ShowPlaylistView, RestrictedView, RegisterProfileView, GoToView, ProfileView, ListProfileView, LikePlaylistView, SearchAddPage


app_name = 'choonz'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('playlist/<slug:playlist_name_slug>/', views.ShowPlaylistView.as_view(), name='show_playlist'),
    path('add_playlist/', views.AddPlaylistView.as_view(), name='add_playlist'),
    path('playlist/<slug:playlist_name_slug>/add_page/', views.AddPageView.as_view(), name='add_page'),
    path('restricted/', views.RestrictedView.as_view(), name='restricted'),
    path('goto/', views.GoToView.as_view(), name='goto'),
    path('register_profile/', views.RegisterProfileView.as_view(), name='register_profile'),
    path('profile/<username>/', views.ProfileView.as_view(), name='profile'),
    path('profiles/', views.ListProfileView.as_view(), name='list_profiles'),
    path('like_playlist/', views.LikePlaylistView.as_view(), name='like_playlist'),
    path('suggest/', views.PlaylistSuggestionView.as_view(), name='suggest'),
    path('search_add_page/', views.SearchAddPage.as_view(), name='search_add_page'),
]