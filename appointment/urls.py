from django.urls import path
from .views import PreacherViews, TopicViews, LocationViews, AppointmentViews,ping
 
urlpatterns = [
#    path('', views.index , name ='index'),
#    path('index.html', views.index , name ='index'),
#    path('api/v1/register/precher', views.register_precher , name ='register'),
   
#    path('artist/<artist_name>', views.song , name ='song'),

   path('api/v1/ping/', ping,name ='ping'),
   path('api/v1/preacher/', PreacherViews.as_view()),
   path('api/v1/preacher/<id>', PreacherViews.as_view()),

   path('api/v1/topic/', TopicViews.as_view()),
   path('api/v1/topic/<id>', TopicViews.as_view()),

   path('api/v1/location/', LocationViews.as_view()),
   path('api/v1/location/<id>', LocationViews.as_view()),

   path('api/v1/schedule/', AppointmentViews.as_view()),

  #  path('Add_songs.html', views.Add_songs , name ='Addsongs'),
 ]

from django.conf import settings
from django.conf.urls.static import static
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)