#!/usr/bin/env bash
set -euo pipefail

API_BASE="${1:-http://localhost:8000}"

echo "[1/4] Checking health endpoint..."
curl -fsS "$API_BASE/health" | tee /tmp/health.json

echo "\n[2/4] Running sample analysis..."
ANALYSIS_RESPONSE=$(curl -fsS -X POST "$API_BASE/analysis/run" \
  -H 'Content-Type: application/json' \
  -d '{"input_type":"coordinates","latitude":-1.286389,"longitude":36.817223}')

echo "$ANALYSIS_RESPONSE" | tee /tmp/analysis_response.json
ANALYSIS_ID=$(python - <<'PY'
import json
with open('/tmp/analysis_response.json','r',encoding='utf-8') as f:
    print(json.load(f)['analysis_id'])
PY
)

echo "\n[3/4] Fetching metrics for analysis: $ANALYSIS_ID"
curl -fsS "$API_BASE/analysis/$ANALYSIS_ID/metrics" | tee /tmp/analysis_metrics.json

echo "\n[4/4] Fetching report metadata..."
curl -fsS "$API_BASE/analysis/$ANALYSIS_ID/report" | tee /tmp/analysis_report.json

echo "\nSmoke test completed successfully."
