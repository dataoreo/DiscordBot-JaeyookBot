import requests
from bs4 import BeautifulSoup as bs
from discord_bot import DiscordBot
import os

def check_menu():
    webhook_url = os.environ.get("DISCORD_WEBHOOK")
    bot = DiscordBot(webhook_url)

    target_url = 'https://www.hanyang.ac.kr/web/www/re15'
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(target_url, headers=headers)
    response.raise_for_status()
    soup = bs(response.text, 'html.parser')

    result = soup.select_one(".menu-detail p")

    if result:
        menu = result.get_text(strip=True).replace(" ", ", ")

        if "제육" in menu:
            alert_text = f"오늘 점심 제육 ㄱ?\n오늘의 메뉴 : {menu}"
            bot.send_message(alert_text)
        else:
            print("오제없(오늘 제육 없다는 뜻)")

    else:
        print("오늘은 주말! 식단이 등록되어 있지 않습니다.")

if __name__ == "__main__":
    check_menu()