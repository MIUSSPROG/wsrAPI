from rest_framework import serializers

from WSR_API.models import Profile, Grade


class ProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class GradeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ('id', 'number', 'letter')


class ProfileGradesSerializer(serializers.ModelSerializer):
    grades = GradeSerializer(many=True)

    class Meta:
        model = Profile
        fields = ('name', 'grades')
