#!/bin/bash
# =============================================================================
# CONNEX Cloud OS Documentation — Git Release & Mintlify Sync Script
# Usage: ./scripts/git-release.sh "commit message" [push|pr|main]
# =============================================================================

set -e

COMMIT_MSG="$1"
ACTION="${2:-push}"

if [ -z "$COMMIT_MSG" ]; then
    echo "❌ Error: Commit message is required."
    echo "   Usage:   ./scripts/git-release.sh \"commit message\" [push|pr|main]"
    echo "   Example: ./scripts/git-release.sh \"docs(architecture): update security kill-switch specs\" push"
    exit 1
fi

if [ ! -f "VERSION" ]; then
    echo "❌ Error: VERSION file not found in root directory."
    exit 1
fi
VERSION=$(cat VERSION | tr -d '[:space:]')
EXPECTED_BRANCH="hs-docs-v${VERSION}"
CURRENT_BRANCH=$(git branch --show-current)

# Run Pre-Release Quality Audit Gate
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [ -f "$SCRIPT_DIR/pre-release-check.sh" ]; then
    "$SCRIPT_DIR/pre-release-check.sh"
fi

if [ "$ACTION" = "push" ]; then
    echo "🚀 [PUSH MODE] Staging and committing to '$CURRENT_BRANCH' with [skip ci]..."
    git add .
    git commit -m "$COMMIT_MSG [skip ci]" || echo "Nothing to commit"
    git push origin "$CURRENT_BRANCH"
    echo "✅ Successfully pushed to origin/$CURRENT_BRANCH with [skip ci]."

elif [ "$ACTION" = "pr" ]; then
    echo "📋 [PR MODE] Creating Pull Request from '$CURRENT_BRANCH' to 'main'..."
    git add .
    git commit -m "$COMMIT_MSG" || echo "Nothing to commit"
    git push origin "$CURRENT_BRANCH"
    
    # Check if gh CLI is available
    if command -v gh &> /dev/null; then
        PR_URL=$(gh pr create --base main --head "$CURRENT_BRANCH" --title "$COMMIT_MSG" --body "Automated SOC 2 Documentation PR for v${VERSION}" 2>&1 || gh pr view --json url -q .url)
        echo ""
        echo "================================================================="
        echo "🔗 [HITL REVIEW REQUIRED] Application PR Link:"
        echo "   $PR_URL"
        echo "================================================================="
    else
        echo "ℹ️  gh CLI not installed. Please create PR from '$CURRENT_BRANCH' to 'main' via GitHub web UI."
    fi

elif [ "$ACTION" = "main" ] || [ "$ACTION" = "prod" ]; then
    echo "🌟 [MAIN/PROD RELEASE MODE] Merging '$CURRENT_BRANCH' into 'main' and syncing Mintlify..."
    git checkout main
    git pull origin main
    git merge "$CURRENT_BRANCH" -m "merge: $COMMIT_MSG (v$VERSION)"
    git tag -a "v$VERSION" -m "Release v$VERSION: $COMMIT_MSG" -f
    git push origin main --tags
    git checkout "$CURRENT_BRANCH"
    echo "🎉 Deployed to main branch! Mintlify portal live synchronization triggered."
else
    echo "❌ Unknown action: $ACTION. Supported: push, pr, main"
    exit 1
fi
