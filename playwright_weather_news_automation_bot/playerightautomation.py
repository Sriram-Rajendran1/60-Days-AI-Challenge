import asyncio
import requests
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

CITY = "Coimbatore"


# ---------------- WEATHER (API - No Playwright) ---------------- #
def get_weather():
    url = f"https://wttr.in/{CITY}?format=j1"
    data = requests.get(url, timeout=10).json()

    temp = data["current_condition"][0]["temp_C"]
    condition = data["current_condition"][0]["weatherDesc"][0]["value"]
    return f"Weather in {CITY}: {temp}°C | {condition}"


# ---------------- NEWS (Requests + BeautifulSoup) ---------------- #
def fetch_news(name, url, selector):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        headlines = [tag.get_text(strip=True) for tag in soup.select(selector)][:5]
        return headlines
    except:
        return [f"Could not fetch news from {name}"]


def get_all_news():
    news_sources = [
        ("Times of India", "https://timesofindia.indiatimes.com/home/headlines", ".w_tle a"),
        ("The Hindu", "https://www.thehindu.com/news/", "h3 a"),
        ("NDTV", "https://www.ndtv.com/latest", ".newsHdng a"),
    ]

    collected = []
    for name, url, selector in news_sources:
        headlines = fetch_news(name, url, selector)
        collected.extend(headlines)

    # remove duplicates + return only top 10 lines
    final_headlines = list(dict.fromkeys(collected))[:10]
    return final_headlines



# ---------------- MAIN ---------------- #
async def main():
    async with async_playwright():
        weather_info = get_weather()
        news = get_all_news()

        print("\n" + "=" * 60)
        print(weather_info)
        print("\n📰 Top News Today:\n")
        for i, headline in enumerate(news, start=1):
            print(f"{i}. {headline}")
        print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
