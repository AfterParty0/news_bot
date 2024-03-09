import json

class CurrenciesService:
    def __init__(self, endpoint: str) -> None:
        self.endpoint = endpoint
    
    async def get_currencies(self) -> list[dict]:
        with open("./api_currencies_example.json", "r", encoding="utf-8") as f:
            data=json.load(f)
                
        return [v for k, v in data["Valute"].items() if k in ["USD", "EUR", "CNY"]]