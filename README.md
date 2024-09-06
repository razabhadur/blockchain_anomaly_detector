# Blockchain Anomaly Detector

## Overview
The Blockchain Anomaly Detector is a Python-based tool designed to detect unusual activities in Ethereum transactions. It leverages machine learning techniques to analyze recent transactions in real-time and identifies anomalies that may indicate suspicious activities, such as fraud or malicious attacks. This tool is particularly useful for blockchain security analysts and researchers who need to monitor and respond to potential threats on the Ethereum network.

## Features
- **Real-time Monitoring**: Continuously monitors the Ethereum blockchain for new blocks and fetches recent transactions.
- **Anomaly Detection**: Uses the Isolation Forest algorithm to detect anomalies in transaction data based on value, gas usage, and gas price.
- **Alert System**: Sends email notifications when anomalies are detected, allowing for quick responses to potential security threats.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/razabhadur/Cross-Chain-Security-Analyzer
    ```
2. Navigate to the project directory:
    ```bash
    cd Cross-Chain-Security-Analyzer
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Update the script with your Infura project ID, email credentials, and email recipient.

## Usage
Run the script to start monitoring the Ethereum blockchain:
```bash
python blockchain_anomaly_detector.py
"""
The script will automatically fetch the latest block, analyze transactions, and detect any anomalies. If anomalies are found, an email alert will be sent with details of the suspicious transactions.

Why This Tool?
This tool is designed to address the increasing need for robust security measures in the blockchain space. With the rise of DeFi and other decentralized applications, the potential for fraud and attacks has grown. The Blockchain Anomaly Detector provides an additional layer of defense by identifying suspicious activities before they can cause significant damage.

Future Improvements
Integration with Other Blockchains: Extend the tool to support other blockchain networks such as Binance Smart Chain or Polkadot.
Enhanced Detection Algorithms: Incorporate more sophisticated machine learning algorithms to improve anomaly detection accuracy.
Dashboard Interface: Develop a web-based dashboard for visualizing detected anomalies and monitoring network activity in real-time.
Contributing
Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for more details.
