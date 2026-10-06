#!/bin/bash
# =============================================================================
# CONNEX Cloud OS Documentation — Pre-Release Quality Audit Gate
# Usage: ./scripts/pre-release-check.sh
# =============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "🔍 Running CONNEX Cloud OS Documentation Pre-Release Audit..."

# 1. Run Python-based Verification Harness
python3 "$SCRIPT_DIR/verify-docs.py"

echo "✅ Pre-release documentation audit passed successfully!"
