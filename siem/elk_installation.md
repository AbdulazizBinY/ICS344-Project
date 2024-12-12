# ELK Stack Installation and Setup Guide

This guide will walk you through installing and setting up the **ELK Stack (Elasticsearch, Logstash, Kibana)** on your machine. 

## Prerequisites:
- Ubuntu/Debian-based operating system.
- Root or sudo privileges on the system.

---

## **1. Install Elasticsearch**

Start by installing Elasticsearch:

```bash
# Add Elasticsearch GPG key
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -

# Install apt transport for HTTPS
sudo apt-get install apt-transport-https -y

# Add the Elasticsearch repository to the sources list
echo "deb https://artifacts.elastic.co/packages/8.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-8.x.list

# Update repositories and install Elasticsearch
sudo apt update && sudo apt install elasticsearch -y
