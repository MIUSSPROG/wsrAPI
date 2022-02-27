# Create your views here.
from rest_framework import generics

from WSR_API.models import Profile
from WSR_API.serializers import ProfileCreateSerializer, GradeCreateSerializer, ProfileGradesSerializer


class ProfileCreateView(generics.CreateAPIView):
    serializer_class = ProfileCreateSerializer


class ProfileListView(generics.ListAPIView):
    serializer_class = ProfileCreateSerializer
    queryset = Profile.objects.all()


class ProfileDeleteView(generics.DestroyAPIView):
    serializer_class = ProfileCreateSerializer
    queryset = Profile.objects.all()


class ProfileUpdateView(generics.UpdateAPIView):
    serializer_class = ProfileCreateSerializer
    queryset = Profile.objects.all()


class GradeCreateView(generics.CreateAPIView):
    serializer_class = GradeCreateSerializer


class ProfileGradesView(generics.RetrieveAPIView):
    serializer_class = ProfileGradesSerializer
    queryset = Profile
