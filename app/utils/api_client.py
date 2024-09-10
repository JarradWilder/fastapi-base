import httpx

class APIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    async def get(self, endpoint: str, params: dict = None):
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}/{endpoint}", params=params)
            response.raise_for_status()  # Raise error if response code is not 2xx
            return response.json()