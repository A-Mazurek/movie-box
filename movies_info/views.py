from rest_framework.generics import ListAPIView, RetrieveAPIView

from movies_info.models import Movie
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movies_info.serializers import MoviesListSerializer


class MoviesListAPIView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MoviesListSerializer


@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        serializer = MoviesListSerializer(movie, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MoviesListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MoviesListSerializer(movie)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MoviesListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
