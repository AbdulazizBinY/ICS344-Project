# Cowrie Honeypot Deployment Guide

This guide explains how to deploy the Cowrie honeypot with SSH set to port `2222`.

## Prerequisites
- A machine running Ubuntu or Debian-based Linux.
- Sudo privileges for installing dependencies and configuring the environment.
- Python 3.6 or higher installed.

---

## Deployment Steps

Follow these commands to install and configure Cowrie:

```bash
# Step 1: Update the system and install required packages
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-venv python3-dev libssl-dev libffi-dev build-essential git -y

# Step 2: Clone the Cowrie repository
cd /opt
sudo git clone https://github.com/cowrie/cowrie.git
cd cowrie

# Step 3: Create and activate a Python virtual environment
python3 -m venv cowrie-env
source cowrie-env/bin/activate

# Step 4: Install Cowrie dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Step 5: Configure Cowrie
# Copy the sample configuration file and set the SSH port to 2222
cp cowrie.cfg.dist cowrie.cfg
sed -i 's/ssh_port = 22/ssh_port = 2222/' cowrie.cfg

# Step 6: Start the Cowrie honeypot
bin/cowrie start

# Step 7: Verify Cowrie is running
bin/cowrie status

# Step 8: View Cowrie logs to ensure activity is being recorded
tail -f log/cowrie.log
