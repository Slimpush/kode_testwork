import requests
from typing import List, Optional


def check_spelling(text: str) -> Optional[List[str]]:
    response = requests.get(
        "https://speller.yandex.net/services/spellservice.json/checkText",
        params={"text": text},
    )
    corrections = response.json()
    return [item["word"] for item in corrections] if corrections else None
