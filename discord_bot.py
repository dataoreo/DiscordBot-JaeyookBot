import logging
 
import requests
 
logger = logging.getLogger(__name__)
 
REQUEST_TIMEOUT = 5
 
 
class DiscordBot:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url
 
    def send_message(self, content):
        data = {
            "content": content,
            "username": "제육 레이더",
        }
 
        try:
            response = requests.post(self.webhook_url, json=data, timeout=REQUEST_TIMEOUT)
        except requests.exceptions.Timeout:
            logger.error("Discord 알림 전송이 시간 초과되었습니다.")
            return
        except requests.exceptions.RequestException as e:
            logger.error(f"Discord 알림 전송 중 오류 발생: {e}")
            return
 
        if response.status_code == 204:
            logger.info("디스코드 알림 발송 성공!")
        else:
            logger.warning(f"발송 실패: {response.status_code}, {response.text}")
 
