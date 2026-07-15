import logging
import os

import requests
from bs4 import BeautifulSoup as bs

from discord_bot import DiscordBot

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

TARGET_URL = "https://www.hanyang.ac.kr/web/www/re15"
HEADERS = {"User-Agent": "Mozilla/5.0"}
REQUEST_TIMEOUT = 10


def fetch_menu_html():
    response = requests.get(TARGET_URL, headers=HEADERS, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()
    return response.text


def check_menu():
    webhook_url = os.environ.get("DISCORD_WEBHOOK")
    if not webhook_url:
        logger.error("DISCORD_WEBHOOK 환경변수가 설정되어 있지 않습니다.")
        return

    bot = DiscordBot(webhook_url)

    try:
        html = fetch_menu_html()
    except requests.exceptions.Timeout:
        logger.error("식단표 요청이 시간 초과되었습니다.")
        return
    except requests.exceptions.RequestException as e:
        logger.error(f"식단표 요청 실패: {e}")
        return

    soup = bs(html, "html.parser")
    result = soup.select_one(".menu-detail p")

    if result is None:
        logger.info("메뉴 요소를 찾지 못했습니다. 주말이거나 페이지 구조가 변경되었을 수 있습니다.")
        return

    menu = result.get_text(strip=True).replace(" ", ", ")
    if not menu:
        logger.warning("메뉴 텍스트가 비어 있습니다. 페이지 구조 변경 여부를 확인하세요.")
        return

    if "제육" in menu:
        alert_text = f"오늘 점심 제육 ㄱ?\n오늘의 메뉴 : {menu}"
    else:
        alert_text = "오제없(오늘 제육 없다는 뜻)"

    bot.send_message(alert_text)


if __name__ == "__main__":
    check_menu()
