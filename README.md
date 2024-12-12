# Honeypot Deployment and SIEM Integration

This repository contains resources for deploying a Cowrie honeypot, integrating it with an ELK Stack SIEM, and running custom scripts for security testing.

---

## Table of Contents
1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Honeypot Deployment](#honeypot-deployment)
4. [ELK Stack Installation](#elk-stack-installation)
5. [Custom Scripts](#custom-scripts)
8. [License](#license)

---

## Overview

This project demonstrates how to:
- Deploy and configure the Cowrie honeypot.
- Install and configure the ELK Stack as a SIEM tool.
- Use custom scripts to test the honeypot and analyze security incidents.
- Collect and analyze logs to improve threat detection and response.

---

## Prerequisites

- **Python 3+** (for scripts)
- **Cowrie Honeypot** (latest version)
- **ELK Stack** (Elasticsearch, Logstash, Kibana)
- **Kali Linux** (optional for attacking tools)
- Basic knowledge of Linux and networking.

---

## Honeypot Deployment

1. Deploy the Cowrie honeypot on your system.
2. Use port 2222 for SSH and 2223 for Telnet.
3. Follow the detailed guide: [Honeypot Deployment Guide](honeypot/deployment_guide.md).

---

## ELK Stack Installation

1. Install and configure the ELK Stack on your server.
2. Set up Elasticsearch, Logstash, and Kibana to collect and analyze Cowrie logs.
3. Refer to the detailed guide: [ELK Installation Guide](siem/elk_installation.md).

---

## Custom Scripts

### 1. **SSH Bruteforce Script**
- File: `scripts/ssh_bruteforce.py`
- Purpose: Test common SSH credentials on the honeypot.
- Usage:
  ```bash
  python3 scripts/ssh_bruteforce.py

### 2. **Telnet Testing Script**
- File: `scripts/telnet_test.py`
- Purpose: Simulate a Telnet session to test logging functionality on the honeypot.
- Usage:
  ```bash
   python3 scripts/telnet_test.py

### 3. **Directory Traversal Testing Script**
- File: `scripts/dir_traversal_test.sh`
- Purpose: Test common SSH credentials on the honeypot.
- Usage:
  ```bash
  python3 scripts/dir_traversal_test.sh
