import json


class CurrenciesService:
    def __init__(self, endpoint: str) -> None:
        self.endpoint = endpoint

    async def get_currencies(
        self, redis
    ) -> list[dict]:
        cache_key = f"currencies:fvhuicur"
        data = await redis.get(cache_key)

        if not data:
            with open(
                "./apiCurrencies.json",
                "r",
                encoding="utf-8",
            ) as f:
                print("Opened file")
                data = json.load(f)
            await redis.set(
                cache_key,
                json.dumps(
                    data, ensure_ascii=False
                ),
                120,
            )

        else:
            data = json.loads(data)

        return [
            v
            for k, v in data["Valute"].items()
            if k in ["USD", "EUR", "CNY"]
        ]
