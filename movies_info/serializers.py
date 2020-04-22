from rest_framework import serializers

from movies_info.models import Movie


class MoviesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'name')
