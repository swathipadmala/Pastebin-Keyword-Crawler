# Pastebin Keyword Crawler 🔍

A Python script to crawl public Pastebin pages and extract pastes containing keywords related to crypto and Telegram activities.

## 📌 Features

- Crawls Pastebin archive page for recent pastes
- Scans each paste for keywords like `crypto`, `bitcoin`, `telegram`, `ethereum`, `wallet`
- Extracts and saves matching URLs with a content snippet
- Stores results in a text file for later analysis

## 🧰 Requirements

- Python 3.6+
- Modules:
  - requests
  - beautifulsoup4

## ⚙️ Setup Instructions

Install the required Python packages:

```bash
pip install -r requirements.txt
