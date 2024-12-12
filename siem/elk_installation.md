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
  ```
---
## **2. Enable and Start Elasticsearch**

Enable Elasticsearch to start on boot and then start it:

  ```bash
# Enable Elasticsearch to start on boot
sudo systemctl enable elasticsearch

# Start Elasticsearch
sudo systemctl start elasticsearch
```

---
## **3. Verify Elasticsearch Installation**

After installation, verify if Elasticsearch is running by visiting:

  ```bash
http://localhost:9200
# You should see a JSON response indicating that Elasticsearch is running.
```

---
## **4. Install Kibana**

Install Kibana, the web interface for viewing logs:

  ```bash
# Install Kibana
sudo apt install kibana -y
```

---
## **5. Enable and Start Kibana**

Enable Kibana to start on boot and then start it:

  ```bash
# Enable Kibana to start on boot
sudo systemctl enable kibana

# Start Kibana
sudo systemctl start kibana
```

---
## **6. Verify Kibana Installation**

After installation, open your browser and go to:

  ```bash
http://localhost:5601
# This should bring up the Kibana dashboard.
```

---
## **7. Install Logstash**

Install Logstash, used for parsing and transforming logs:

  ```bash
# Install Logstash
sudo apt install logstash -y
```

---
## **8. Enable and Start Logstash**

Enable Logstash to start on boot and then start it:

  ```bash
# Enable Logstash to start on boot
sudo systemctl enable logstash

# Start Logstash
sudo systemctl start logstash
```
