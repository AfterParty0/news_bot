import json


class NewsService:
    def __init__(
        self, endpoint: str, api_key: str
    ) -> None:
        self.endpoint = endpoint
        self.api_key = api_key

    async def get_news(
        self,
        redis,
        q: str = "Russia",
        lang: str = "ru",
        country: str = "ru",
        max: int = 5,
    ) -> list[dict]:
        cache_key = (
            f"news:{q=},{lang=},{country=},{max=}"
        )
        data = await redis.get(cache_key)

        if not data:
            with open(
                "./apiNews.json",
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

        return [v for v in data["articles"]]
