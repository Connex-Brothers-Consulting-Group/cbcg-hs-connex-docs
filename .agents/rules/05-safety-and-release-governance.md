# Rule 05: Safety & Release Governance (SOC 2 Type II Protocol)

## 1. Absolute Safety Gates
- **Destructive Git Commands Banned**: `git reset --hard`, destructive checkout, or force push are strictly prohibited.
- **Local Server Prohibition**: The agent must NEVER launch `mintlify dev` or local servers via background commands.
- **Browser Subagent Prohibition**: The agent must NEVER launch automated browser windows without explicit request.

## 2. NEXUS LAB 126 3대 무결성 공학 철칙 (Anti-Fraud Engineering Standards)
1. **임의의 `sleep()`을 통한 동기화 영구 금지**:
   - 스크립트나 코드에 임의의 `sleep()`을 넣는 행위는 사기(Fraud)입니다. 시간차는 프로토콜 및 결정론적 검증으로 해결합니다.
2. **핵심 상태 변경의 백그라운드 방치 금지**:
   - 상태 변경 및 파일 수정 후 검증을 방치하지 않고 확실히 완료를 확인합니다.
3. **Mock 테스트 맹신 금지 & 실제 실측 검증**:
   - `./scripts/verify-docs.py`를 통해 실제 41개 MDX 파일과 `docs.json`, `style.css`의 무결성을 숫자로 직접 증명합니다.

## 3. Gitflow Release Ritual (`./scripts/git-release.sh`)
- **Push Mode**: `./scripts/git-release.sh "<msg>" push` (working branch push with `[skip ci]`).
- **PR Mode**: `./scripts/git-release.sh "<msg>" pr` (creates GitHub PR for HITL human review).
- **Main Mode**: `./scripts/git-release.sh "<msg>" main` (merges to `main`, tags, and deploys live).
