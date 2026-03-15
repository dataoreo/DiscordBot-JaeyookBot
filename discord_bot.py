import requests

class DiscordBot:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def send_message(self, content):
        data = {
            "content": content,
            "username": "제육 레이더"
        }
        
        try:
            response = requests.post(self.webhook_url, json=data)
            if response.status_code == 204:
                print("디스코드 알림 발송 성공!")
            else:
                print(f"발송 실패: {response.status_code}, {response.text}")

        except Exception as e:
            print(f"오류 발생: {e}")