# To-do 리스트 웹 애플리케이션

이 프로젝트는 간단한 To-do 리스트 웹 애플리케이션입니다. 사용자는 할 일을 추가하고 삭제할 수 있습니다. 이 애플리케이션은 Tailwind CSS를 사용하여 스타일링되었습니다.

## 프로젝트 구조

```
todo-list
├── src
│   ├── index.html        # 메인 HTML 문서
│   └── styles
│       └── tailwind.css  # Tailwind CSS 스타일
├── tailwind.config.js    # Tailwind CSS 설정 파일
├── package.json          # npm 설정 파일
└── README.md             # 프로젝트 문서
```

## 설치 및 실행

1. **리포지토리 클론**
   ```bash
   git clone <repository-url>
   cd todo-list
   ```

2. **의존성 설치**
   ```bash
   npm install
   ```

3. **Tailwind CSS 빌드**
   ```bash
   npx tailwindcss -i ./src/styles/tailwind.css -o ./dist/output.css --watch
   ```

4. **애플리케이션 실행**
   - `src/index.html` 파일을 웹 브라우저에서 열어 애플리케이션을 사용합니다.

## 사용 방법

- 새로운 할 일을 입력하고 "추가" 버튼을 클릭하여 목록에 추가합니다.
- 각 할 일 항목 옆에 있는 "삭제" 버튼을 클릭하여 해당 항목을 삭제합니다.

## 기여

기여를 원하시는 분은 이 리포지토리를 포크한 후, 변경 사항을 커밋하고 풀 리퀘스트를 제출해 주세요.

## 라이센스

이 프로젝트는 MIT 라이센스 하에 배포됩니다.