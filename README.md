---

# Ethereum Node Monitoring Infrastructure

**A full-stack, containerized Ethereum Sepolia network monitoring setup demonstrating hands-on DevOps and blockchain infrastructure skills.**

---

## 🚀 Project Summary

This project demonstrates **practical DevOps expertise on Ethereum infrastructure**, including:

* Deployment of **execution layer (Geth)** and **consensus layer (Lighthouse) nodes** using Docker
* End-to-end **monitoring setup** with Prometheus and Grafana
* Automated metrics collection for **node health, block synchronization, and validator activity**
* Ability to **simulate transactions** to monitor transaction throughput

> Designed and implemented **from scratch**, progressing from a development test environment (block number tracking) to a production-grade, full Sepolia monitoring environment.

---

## 🧩 Key Contributions

* **Dockerized Ethereum nodes**: Configured Geth and Lighthouse in isolated containers, exposing RPC, metrics, and consensus endpoints
* **Metrics & Monitoring**:

  * Prometheus scraping for **execution and consensus layers**
  * Grafana dashboards visualizing **blocks, peers, transactions, validator performance**
* **Debugging & Sync Optimization**: Monitored syncing issues, analyzed logs, optimized volumes and network settings
* **Security Awareness**: Managed JWT authentication between execution and consensus nodes for validator integration
* **Automation**: Set up scripts for node initialization and environment teardown

> This project **demonstrates end-to-end understanding** of Ethereum node operation, monitoring, and DevOps automation.

---

## 📂 Project Structure

```
eth-auto-infra/
├── docker/
│   ├── docker-compose-geth.yaml        # Geth + Lighthouse node definitions
│   ├── docker-compose-monitor.yaml    # Prometheus + Grafana
├── monitoring/
│   ├── prometheus.yaml
│   └── grafana/                        # Grafana persistent volume
├── data/
│   ├── geth/                            # Geth blockchain data
│   └── lighthouse/                      # Lighthouse consensus data
├── scripts/
│   └── setup.py                         # Automation scripts
└── README.md
```

---

## 🛠 Tech Stack

| Component               | Purpose                                                       |
| ----------------------- | ------------------------------------------------------------- |
| Geth                    | Ethereum execution layer node                                 |
| Lighthouse              | Ethereum consensus layer node                                 |
| Docker / Docker Compose | Containerized orchestration and environment isolation         |
| Prometheus              | Metrics collection for nodes                                  |
| Grafana                 | Visualization of blockchain metrics and validator performance |
| Linux CLI / Bash        | Automation and debugging                                      |

---

## ⚡ Development Environment (Test)

**Purpose:** Validate blockchain connectivity, RPC endpoints, and basic metrics collection.

* Tracks only **block number** in Grafana
* Useful for **quick testing** before production-grade setup

```bash
cd docker
docker-compose -f docker-compose-geth.yaml up -d
docker-compose -f docker-compose-monitor.yaml up -d
```

**Screenshots**:
![Block Number Test SS](INSERT_SS_HERE)

> ✅ Shows ability to set up nodes, expose metrics, and integrate dashboards.

---

## 🌐 Production-Grade Sepolia Setup

**Purpose:** Realistic Ethereum infrastructure for DevOps demonstration

* Full **snap sync Geth node**
* Lighthouse beacon node with **JWT authentication**
* Metrics scraped by Prometheus from both nodes
* Grafana dashboards tracking:

  * Block height and syncing progress
  * Peer connectivity
  * Validator activity
  * Transaction throughput

**Usage:**

```bash
cd docker
docker-compose -f docker-compose-geth.yaml up -d
docker-compose -f docker-compose-monitor.yaml up -d
```

**Screenshots**:

* Geth Metrics: ![Geth Metrics SS](INSERT_SS_HERE)
* Lighthouse Metrics: ![Lighthouse Metrics SS](INSERT_SS_HERE)
* Grafana Dashboard: ![Dashboard SS](INSERT_SS_HERE)

> ✅ Shows ability to deploy production-grade blockchain nodes with monitoring and security best practices.

---

## 🎯 Highlights

* **End-to-end DevOps skills**: Docker, metrics monitoring, log analysis, automated deployment
* **Web3 readiness**: Hands-on with Ethereum execution & consensus nodes
* **Problem-solving**: Debugged syncing issues, optimized RPC/metrics endpoints, managed peer connectivity
* **Metrics-driven mindset**: Created dashboards for real-time monitoring of blockchain activity
* **Security aware**: Configured JWT between execution and consensus nodes

> This project clearly demonstrates **practical Ethereum DevOps experience**, a skill set Ethereum Foundation actively looks for in interns.

---

## 📝 Future Improvements

* Integrate **transaction simulation** to show live transaction rate metrics
* Add **alerts** for node lag or validator downtime
* Extend to **mainnet-compatible configuration**
* Automate Grafana dashboard provisioning via **JSON templates**

---

## ⚙️ Prerequisites

* Docker & Docker Compose
* Linux/macOS (or Windows WSL2)
* Optional: Python 3.x for automation scripts

---
