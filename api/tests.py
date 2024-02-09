from unittest.mock import patch
from rest_framework.test import APITestCase
from rest_framework import status
from IMDBMovies.settings import env


api_key = env.str('OMIDB_SECRET_KEY')
omidb_base_url=env.str('OMIDB_BASE_URL')



class FetchMoviesApiViewTest(APITestCase):
    @patch('api.views.FetchOMDBMovies')
    def test_fetch_movies_with_identifier(self, mock_fetch_omdb_movies):
        mock_instance = mock_fetch_omdb_movies.return_value
        mock_instance.get.return_value = {'fake_data': 'fake_value'}

        api_key =api_key
        identifier = 'insecure'

        response = self.client.get(f'/detail/?i={identifier}&apikey={api_key}')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"message": "data successfully fetched", "data": {'fake_data': 'fake_value'}})
        mock_instance.get.assert_called_once_with(identifier=identifier, search_title=None)

    @patch('api.views.FetchOMDBMovies')
    def test_fetch_movies_with_search_title(self, mock_fetch_omdb_movies):
        mock_instance = mock_fetch_omdb_movies.return_value
        mock_instance.get.return_value = {'fake_data': 'fake_value'}

        api_key = api_key
        search_title = 'young sheldon'

        response = self.client.get(f'/detail/?t={search_title}&apikey={api_key}')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"message": "data successfully fetched", "data": {'fake_data': 'fake_value'}})
        mock_instance.get.assert_called_once_with(identifier=None, search_title=search_title)

    