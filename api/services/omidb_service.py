from IMDBMovies.settings import env
import requests


omidb_base_url=env.str('OMIDB_BASE_URL')
api_key=env.str('OMIDB_SECRET_KEY')



class FetchOMDBMovies:
    def __init__(self, api_key):
        self.omdb_base_url =omidb_base_url
        self.api_key = api_key

    def get(self, identifier=None, search_title=None, **params):
        if not identifier and not search_title:
            raise ValueError("Either IMDb ID (i) or movie title (t) must be provided.")

        params.update({'i': identifier, 't': search_title})

        params['apikey'] = self.api_key

        url = f"{self.omdb_base_url}?" + "&".join([f"{key}={value}" for key, value in params.items()])
        print("url,ur;",url)

        response = requests.get(url)
        print("response,response")

        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Error {response.status_code}: {response.text}"}

# api_key = "your_api_key"
# fetcher = FetchOMDBMovies(api_key)

# # Search by IMDb ID with additional parameters
# result_by_id_with_params = fetcher.get(identifier="tt1285016", type="movie", year="2022", plot="full")
# print(result_by_id_with_params)

# # Search by movie title with additional parameters
# result_by_title_with_params = fetcher.get(search_title="Bridgerton", type="series", r="json")
# print(result_by_title_with_params)
