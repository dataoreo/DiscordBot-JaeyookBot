<div align="center">
  <br>
  <h1>🍖 [Toy Project] 창보제육 알리미 🍖</h1> 
  <p><strong>"디스코드 알림 하나로 오늘 점심은 창보제육 바로 결정!"</strong></p>
  <br>
</div>

## 📌 프로젝트 개요

### **창보 학식의 명물, "창보제육"!**
- 매일 아침 10시, 창보 점심 메뉴에 제육이 포함되어 있다면 디스코드 알림을 통해 창보제육 소식을 전합니다.

<br>

## ⏰ 개발 기간
- **2026.03.15 ~ 2026.03.16** (2일간)

<br>

## 🏗 주요 기능

| 기능 | 설명 | 기술 스택 |
| :--- | :--- | :--- |
| **자동 식단 스캔** | 창보 식당의 점심 메뉴 HTML 데이터 수집 | ![BS4](https://img.shields.io/badge/BeautifulSoup4-4EAA25?style=flat-square&logo=Python&logoColor=white) |
| **제육 키워드 필터링** | 메뉴 중 '제육'이 포함되었는지 확인 | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white) |
| **디스코드 푸시 알림** | 오전 10시 정각에 디스코드 알림 발송 | ![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white) ![Discord](https://img.shields.io/badge/Discord%20API-5865F2?style=flat-square&logo=discord&logoColor=white) |

<br>

## 📂 폴더 구조

```text
├── .github/
│   └── workflows/
│       └── jeyook.yml        # GitHub Actions를 이용한 자동 실행 스케줄러 (매일 10시)
├── daily_crawling.py         # BeautifulSoup4를 활용한 식단 크롤링 메인 로직
├── discord_bot.py            # Discord Webhook API 연동 및 알림 발송 모듈
├── .gitignore                
└── README.md                 

