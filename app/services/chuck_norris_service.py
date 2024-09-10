from utils.api_client import APIClient

class ChuckNorrisService:
    def __init__(self):
        self.api_client = APIClient("https://api.chucknorris.io/jokes")

    async def get_random_joke(self):
        # Call the API and return the random joke
        response = await self.api_client.get("random")

        return response["value"]
    
# Initialize the service
chuck_norris_service = ChuckNorrisService()