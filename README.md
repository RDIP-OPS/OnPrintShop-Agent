# OnPrintShop AI Agent

A custom AI assistant for OnPrintShop powered by LangChain, FAISS, and OpenAI.

## 🧩 Features
- Dynamic scraping (Selenium-based or static)
- Vector search over official docs
- FastAPI API to query agent
- Ready to deploy to Render / Railway

## 🚀 Setup

```bash
git clone https://github.com/RDIP-OPS/OnPrintShop-Agent.git
cd OnPrintShop-Agent
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# OnPrintShop AI Agent 🤖🖨️

An AI-powered assistant for Replica Digital Ink, built to support setup, SEO, pricing, and product management on OnPrintShop.

## 🔍 Features

- Grounded Q&A on OnPrintShop documentation
- LangChain + OpenAI + FAISS powered backend
- Built with FastAPI for clean API endpoints
- Custom knowledge from support guides and FAQs

## 📦 Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload