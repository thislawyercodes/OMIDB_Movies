from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from api.services.omidb_service import FetchOMDBMovies
from rest_framework import status
from IMDBMovies.settings import env

class FetchMoviesApiView(ListAPIView):

     def get(self, request, *args, **kwargs):
        api_key = env.str('OMIDB_SECRET_KEY')
        identifier = request.query_params.get('i')
        search_title = request.query_params.get('t')

        if not identifier and not search_title:
            return Response({"error": "Either IMDb ID (i) or movie title (t) must be provided."}, status=400)

        omdb_fetcher = FetchOMDBMovies(api_key)

        try:
            data = omdb_fetcher.get(identifier=identifier, search_title=search_title)

            if data:
                return Response({"message": "data successfully fetched", "data": data}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Error occurred while fetching movie data"}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(f"Error fetching movie data: {str(e)}")
            return Response({"message": "Error occurred while fetching movie data"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)