from django.urls import path

from WSR_API.views import ProfileCreateView, ProfileListView, ProfileDeleteView, ProfileUpdateView, GradeCreateView, \
    ProfileGradesView

urlpatterns = [

    path("profile", ProfileCreateView.as_view()),
    path('profile/all', ProfileListView.as_view()),
    path('profile/<int:pk>', ProfileDeleteView.as_view()),
    path('profile/update/<int:pk>', ProfileUpdateView.as_view()),
    path('grade', GradeCreateView.as_view()),
    path('profile/<int:pk>/grades', ProfileGradesView.as_view())
]