# Drill 09

방향키로 소년을 상하좌우로 움직이는 `pico2d` 과제입니다.

## 실행

```powershell
python character_runs_esc.py
```

- 방향키: 소년을 상하좌우로 이동
- `Esc`: 종료
- 키를 떼면 마지막 좌우 방향을 바라보며 IDLE 애니메이션 재생
- 스프라이트의 가장자리가 화면 밖으로 나가지 않도록 이동 범위 제한

## 테스트

```powershell
python -m unittest -v
```

