#!/usr/bin/env python3
import requests
import time

# -------- CONFIG --------
GETH_RPC = "http://localhost:8545"       # Geth RPC endpoint
LIGHTHOUSE_METRICS = "http://localhost:5054/metrics"  # Lighthouse Prometheus metrics
INTERVAL = 10  # seconds between polls

def hex_to_int(h):
    return int(h, 16)

def get_geth_status():
    # Current block
    payload = {"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}
    r = requests.post(GETH_RPC, json=payload)
    block = hex_to_int(r.json().get("result", "0x0"))

    # Peer count
    payload = {"jsonrpc":"2.0","method":"net_peerCount","params":[],"id":1}
    r = requests.post(GETH_RPC, json=payload)
    peers = hex_to_int(r.json().get("result", "0x0"))

    # Pending transactions
    payload = {"jsonrpc":"2.0","method":"eth_pendingTransactions","params":[],"id":1}
    r = requests.post(GETH_RPC, json=payload)
    pending = len(r.json().get("result", []))

    return block, peers, pending

def get_lighthouse_status():
    try:
        r = requests.get(LIGHTHOUSE_METRICS)
        lines = r.text.splitlines()
        last_received_block = 0
        head_block = 0
        for line in lines:
            if line.startswith("beacon_chain_head_slot"):
                head_block = int(float(line.split()[1]))
            if line.startswith("beacon_chain_finalized_checkpoint_slot"):
                last_received_block = int(float(line.split()[1]))
        return head_block, last_received_block
    except Exception:
        return 0, 0

if __name__ == "__main__":
    print("Monitoring Geth + Lighthouse metrics (Ctrl+C to exit)")
    while True:
        geth_block, geth_peers, geth_pending = get_geth_status()
        lh_head, lh_last = get_lighthouse_status()
        print(f"⛓ Geth  | Block: {geth_block} | Peers: {geth_peers} | Pending Tx: {geth_pending}")
        print(f"🌉 Lighthouse | Head Block: {lh_head} | Last Received Block: {lh_last}")
        print("-"*80)
        time.sleep(INTERVAL)

