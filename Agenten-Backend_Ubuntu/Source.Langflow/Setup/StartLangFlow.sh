#!/bin/bash

cd /home/kai || exit 1

cleanup() {
    echo "Stopping LangFlow..."
    pkill -f "uv run langflow"
    exit 0
}

source /home/kai/.venv/bin/activate

trap cleanup SIGINT SIGTERM
uv run langflow run --env-file ~/.env
# uv run langflow run --components-path /home/kai/langflow/components/custom/ --env-file ~/.env

## Update auf die letzte Version
# source /home/kai/.venv/bin/activate
# uv pip install langflow -U
