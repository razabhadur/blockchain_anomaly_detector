import time
import json
import requests
import numpy as np
import pandas as pd
from datetime import datetime
from sklearn.ensemble import IsolationForest
from web3 import Web3
import smtplib
from email.mime.text import MIMEText

# Step 1: Connect to Ethereum network (using Infura)
infura_url = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
web3 = Web3(Web3.HTTPProvider(infura_url))

if web3.isConnected():
    print("Connected to Ethereum network")
else:
    print("Failed to connect to Ethereum network")
    exit()

# Step 2: Function to fetch recent transactions from the latest block
def fetch_transactions(block_number):
    block = web3.eth.getBlock(block_number, full_transactions=True)
    transactions = block.transactions
    tx_data = []
    for tx in transactions:
        tx_data.append({
            'hash': tx.hash.hex(),
            'from': tx['from'],
            'to': tx['to'],
            'value': web3.fromWei(tx['value'], 'ether'),
            'gas': tx['gas'],
            'gas_price': web3.fromWei(tx['gasPrice'], 'gwei'),
            'timestamp': datetime.fromtimestamp(block.timestamp).strftime('%Y-%m-%d %H:%M:%S')
        })
    return pd.DataFrame(tx_data)

# Step 3: Anomaly Detection using Isolation Forest
def detect_anomalies(df):
    model = IsolationForest(contamination=0.01)
    features = df[['value', 'gas', 'gas_price']]
    model.fit(features)
    df['anomaly'] = model.predict(features)
    anomalies = df[df['anomaly'] == -1]
    return anomalies

# Step 4: Alerting system to send email notifications
def send_alert(anomalies, block_number):
    sender = "your_email@gmail.com"
    receiver = "alert_receiver@gmail.com"
    subject = f"Anomalies detected in block {block_number}"
    body = f"Anomalies detected:\n{anomalies.to_string(index=False)}"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.login(sender, "your_email_password")
        smtp_server.sendmail(sender, receiver, msg.as_string())
        smtp_server.close()
        print(f"Alert sent for block {block_number}")
    except Exception as e:
        print(f"Failed to send alert: {e}")

# Step 5: Real-time monitoring loop
def monitor_blocks():
    latest_block = web3.eth.blockNumber
    print(f"Starting monitoring from block: {latest_block}")

    while True:
        current_block = web3.eth.blockNumber
        if current_block > latest_block:
            df = fetch_transactions(current_block)
            anomalies = detect_anomalies(df)
            
            if not anomalies.empty:
                print(f"Anomalies detected in block {current_block}:")
                print(anomalies)
                send_alert(anomalies, current_block)

            latest_block = current_block
        else:
            print("No new blocks. Waiting...")

        # Wait for a new block (average block time ~15 seconds)
        time.sleep(15)

# Start monitoring
monitor_blocks()

