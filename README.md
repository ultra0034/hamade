# HAMADE (東和電機製作所) — 사이트 리뉴얼 시안

https://towa-denki.co.jp/ 의 디자인 리뉴얼 시안입니다. (흰색 + 네이비, 스크롤 연출 중심)

- `index.html` — 메인 페이지
- `history.html` — HAMADEの歴史 (연혁)
- `video.mp4` — 히어로 영상 (HTML과 같은 폴더에 있어야 재생됨)
- `gen.py`, `ref.css`, `ref.js` — 소스. `python3 gen.py` 실행 시 두 HTML을 다시 생성 (CSS/JS를 HTML 안에 인라인)

## 보는 법
```bash
python3 -m http.server 8000
# http://localhost:8000/index.html
```

※ 일부 본문 카피는 시안용 임시 문구입니다.
