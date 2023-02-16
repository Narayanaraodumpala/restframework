from django.urls import path,include
from albums.views import MusicianListViewset,UpdateMusicianView,AlbumListView,AlbumView,QuestionViewsets,ChoiceViewsets,ModulesViewSet,StudentsViewSet

from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('questionviewsets',QuestionViewsets,basename='questionviewsets')
router.register('choiceviesets',ChoiceViewsets,basename='choiceviesets')
router.register('musicians',MusicianListViewset,basename='musicians')
router.register('albums',AlbumListView,basename='albums'),
router.register('student',StudentsViewSet,basename='student'),
router.register('module',ModulesViewSet,basename='module')

urlpatterns = [
        #path('musicians', MusicianListView.as_view()),
        # path('albums', AlbumListView.as_view()),
path('updatemusicians/<int:pk>', UpdateMusicianView.as_view()),

path('albums/<int:pk>', AlbumView.as_view()),
path('',include(router.urls))
]
