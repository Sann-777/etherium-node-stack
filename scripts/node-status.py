#!/usr/bin/env python3
"""
Simple JSON-RPC check script for an Ethereum JSON-RPC endpoint.
Run: python3 node_status.py --rpc http://localhost:8545
"""
import argparse
import requests
import time


def hex_to_int(h: str) -> int:
    return int(h, 16)


def get_block_number(rpc_url: str, timeout: int = 5) -> int:
    payload = {"jsonrpc": "2.0", "method": "eth_blockNumber", "params": [], "id": 1}
    res = requests.post(rpc_url, json=payload, timeout=timeout)
    res.raise_for_status()
    data = res.json()
    return hex_to_int(data["result"]) if "result" in data else -1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--rpc", default="http://localhost:8545", help="RPC endpoint URL")
    parser.add_argument("--interval", type=int, default=60, help="Poll interval seconds")
    args = parser.parse_args()

    last_block = -1
    while True:
        try:
            block = get_block_number(args.rpc)
            ts = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
            print(f"[{ts}] Block: {block}")
            if last_block != -1 and block <= last_block:
                print(f"{ts} WARNING: Block did not advance (last={last_block} current={block})")
            last_block = block
        except Exception as e:
            print(f"Error contacting RPC {args.rpc}: {e}")
        time.sleep(args.interval)
