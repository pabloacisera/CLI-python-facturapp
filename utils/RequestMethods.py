import requests
from config.config import Config

class RequestMethods:
    @staticmethod
    def post(endpoint, data=None, headers=None):
        url = f"{Config.BASE_URL}/{endpoint}"
        try:
            response = requests.post(
                url,
                json=data,
                headers=headers or {}
            )
            response.raise_for_status()
            return response.json() if response.content else None
        except requests.exceptions.RequestException as e:
            print(f"Error en POST a {url}: {e}")
            return None

    @staticmethod
    def get(endpoint, headers=None):
        url = f"{Config.BASE_URL}/{endpoint}"
        try:
            response = requests.get(
                url,
                headers=headers or {}
            )
            response.raise_for_status()
            return response.json() if response.content else None
        except requests.exceptions.RequestException as e:
            print(f"Error en GET a {url}: {e}")
            return None