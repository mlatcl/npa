#!/bin/bash
# Compile lectures listed in lectures.csv (skip header row).
set -euo pipefail

cd "$(dirname "$0")"

compile_list() {
    local csv="$1"
    local skip=true
    local stub
    while IFS= read -r stub || [[ -n "$stub" ]]; do
        stub="${stub//$'\r'/}"
        [[ -z "$stub" ]] && continue
        if $skip; then
            skip=false
            continue
        fi
        echo "maketalk ${stub}.md"
        maketalk "${stub}.md"
    done < "$csv"
}

compile_list lectures.csv
if [[ -f worksheets.csv ]]; then
    compile_list worksheets.csv
fi
