---
name: castle-builder
description: Visual software architecture supervisor and castle metaphor builder for vibe coding. Scans codebase into 4 layers (Underground Core/DB, Castle Wall API/Auth, Keep Business Logic, Watchtower UI), visualizes project progress and structural risks, and warns before cascading collapse.
---

# Castle Builder (아키텍처 감리 및 성채 빌더)

바이브 코딩 환경에서 시스템 붕괴를 예방하고 아키텍처를 직관적인 '성(Castle)' 구조로 시각화·감리하는 에이전트 스킬.

## 4대 아키텍처 계층 매핑

1. **지하 암반 및 기초 (Underground / Core & DB)**: DB 스키마, ORM, 코어 인프라, 백엔드 데몬
2. **외벽 및 성문 (Walls & Gates / Auth & API)**: 인증/인가(JWT/Session), API 게이트웨이, 라우터, 에러 핸들링
3. **본관 내성 (Keep / Business Logic)**: 핵심 도메인 로직, 데이터 변환/비즈니스 엔진
4. **상층 망루 (Watchtower / UI & Client)**: 프론트엔드 컴포넌트, 대시보드 뷰, 사용자 인터랙션

## 실행 워크플로우

1. **프로젝트 스캔**:
   - `python scanner.py`를 실행하여 파일 구조와 의존성 요약본(`castle_summary.json`)을 생성합니다.
   - 신규 프로젝트일 경우 사용자 요구사항 대화로부터 4대 계층 초기 청사진을 도출합니다.

2. **아키텍처 감리 및 위험도 계산**:
   - 의존성 및 코드 변경 요청을 평가하여 안정도(0~100%)와 결함 유형을 분류합니다:
     - **기초 결여**: 하부 DB/인증 없이 상층 UI 강행 -> 공중 부양 경고
     - **스파게티 결합**: UI에서 DB 직접 참조 / 순환 참조 -> 썩은 사다리/밧줄 경고
     - **내력벽 철거**: 핵심 테이블/코어 스키마 변경 시 상부 모듈 연쇄 붕괴 경고
   - `castle_state.json`에 상태를 갱신합니다.

3. **시각화 뷰어 제공**:
   - `viewer.html`을 브라우저에 열어 성의 축조 상태와 HUD 계측기(안정도 %, 내구도, 붕괴 위험 구역)를 확인하도록 안내합니다.

4. **의사결정 게이트 (위험 감지 시)**:
   - 사용자에게 3가지 분기를 제시하고 승인을 받은 후 코딩 에이전트에게 제약 가드레일을 주입합니다:
     - [1] 임시 비계 받치기 (일단 빠르게 진행, 균열 경고 유지)
     - [2] 기초 리팩토링 후 증축 (권장)
     - [3] 강행 (붕괴 위험 감수)
