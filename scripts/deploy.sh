#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ANSIBLE_DIR="$ROOT_DIR/ansible"

if [ -z "${1-}" ]; then
  echo "Usage: ./deploy.sh <inventory_ip_or_group>"
  echo "Example: ./deploy.sh eth_nodes"
  exit 1
fi

TARGET="$1"

ansible-playbook -i "$ANSIBLE_DIR/inventory.ini" "$ANSIBLE_DIR/playbook.yaml" --limit "$TARGET"

