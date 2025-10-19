#!/usr/bin/env bash
set -euo pipefail

# This script stops and removes docker stacks on the remote server using ansible ad-hoc commands
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ANSIBLE_DIR="$ROOT_DIR/ansible"

ansible -i "$ANSIBLE_DIR/inventory.ini" eth_nodes -m shell -a "cd /opt/eth-auto-infra/docker && docker compose -f docker-compose-geth.yml down || true"
ansible -i "$ANSIBLE_DIR/inventory.ini" eth_nodes -m shell -a "cd /opt/eth-auto-infra/docker && docker compose -f docker-compose-grafana-prometheus.yml down || true"
