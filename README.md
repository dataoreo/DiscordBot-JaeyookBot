<div align="center">
  <br>
  <h1>🍖 [Toy Project] 창보제육 알리미 🍖</h1> 
  <p><strong>"디스코드 알림 하나로 오늘 점심은 창보제육 바로 결정"</strong></p>
  <br>
</div>

## 📌 프로젝트 개요

### **창보 학식의 명물, "창보제육"**
- 매일 아침 10시, 창보 점심 메뉴에 제육이 포함되어 있다면 디스코드 알림을 통해 창보제육 소식을 전합니다.

- 디스코드 채널 링크 : 추후 공개
<br>

## 🏗 주요 기능

| 기능 | 설명 | 기술 스택 |
| :--- | :--- | :--- |
| **자동 식단 스캔** | 창보 식당의 점심 메뉴 HTML 데이터 수집 및 파싱 | ![BS4](https://img.shields.io/badge/BeautifulSoup4-4EAA25?style=flat-square&logo=Python&logoColor=white) |
| **제육 키워드 필터링** | 메뉴 중 '제육'이 포함되었는지 정교하게 확인 | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white) |
| **서버리스 스케줄러** | YAML 스케줄링 기반 매일 오전 10시 자동 실행 | ![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white) |
| **디스코드 푸시 알림** | 제육 확인 시 Discord Webhook을 통한 즉시 알림 | ![Discord](https://img.shields.io/badge/Discord%20API-5865F2?style=flat-square&logo=Discord&logoColor=white) |

> **💡 주요 전략**
> - **무료 서버리스 자동화**: `GitHub Actions`를 활용해 컴퓨터를 켜두지 않아도 서버 유지비 없이 정해진 시간에 클라우드 서버가 자동으로 작동된다.

<br>

## 📂 폴더 구조

```text
├── .github/
│   └── workflows/
│       └── jeyook.yml        # GitHub Actions를 이용한 자동 실행 스케줄러 (매일 오전 10시)
├── daily_crawling.py         # BeautifulSoup4를 활용한 식단 크롤링 메인 로직
├── discord_bot.py            # Discord Webhook API 연동 및 알림 발송 모듈
├── .gitignore                
└── README.md                 
```

<br>

## ⏰ 개발 기간 및 참여 인원
- **2026.03.15 ~ 2026.03.16** (2일간)
- 참여 인원 : 1명

<br>

## 🌱 후기

본 토이 프로젝트에서 `YAML`과`GitHub Actions`를 처음으로 직접 다뤄보았다. 프로젝트를 통해 배운 점을 아래에 정리해보았다.

- **서버 없는 자동화 (Serverless + Free Cost)**
  - `GitHub Actions`를 이용해 정해진 시간에 코드가 스스로 작동하게 만드는 법을 배웠다.
  - `GitHub Actions`를 이용해 물리적 공간의 제약과 비용 부담이 없는 자동화 환경을 구축했다는 점에 큰 가치를 두었다.

- **YAML을 통한 환경 설정**
  - Python 설치, 라이브러리 세팅, 실행 스케줄링 등을 `.yml` 파일에 직접 작성해 보았다.
  - 이 과정을 통해 소프트웨어 작동에 필요한 모든 설정을 데이터로 구조화하고 코드로 관리하는 `YAML`의 역할을 이해하게 되었다.

- **GitHub Secrets**
  - `GitHub Secrets`를 이용해 Discord Weebhook URl과 같은 민감한 정보를 Github 코드에 노출하지 않고 프로그램을 구동하는 방법을 배웠다.

