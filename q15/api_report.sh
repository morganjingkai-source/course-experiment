#!/bin/bash

# 获取数据并生成 Markdown 报告
curl -fsS http://127.0.0.1:8000/packages.json | \
jq -r '
  map(select(.status == "active" and .downloads >= 100)) |
  sort_by(-.downloads, .name) |
  ["# Package Report", "", "| Name | Version | Downloads |", "|------|---------|-----------|"] + 
  map("| \(.name) | \(.version) | \(.downloads) |") |
  .[]
' > summary.md
