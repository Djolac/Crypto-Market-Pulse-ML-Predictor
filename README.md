# Crypto MarketPulse ML Platform

A real-time machine learning system for streaming crypto market data, generating features, training predictive models, and serving live forecasts.

This project demonstrates a full end-to-end ML engineering architecture:
- Real-time data ingestion from WebSocket APIs  
- Kafka-based streaming feature pipeline  
- ML training pipeline with experiment tracking  
- Model registry for controlled deployment  
- Real-time inference microservice  
- Streamlit dashboard for visualization  
- Dockerized microservices & reproducible environments (uv + pyproject.toml)  
- Production-style monitoring & scaling

---

## 🚀 Project Overview

Crypto MarketPulse is a real-time ML system built to:
- Ingest live crypto price data
- Compute streaming features (returns, volatility, indicators)
- Train forecasting models
- Serve live predictions through a FastAPI microservice
- Visualize predictions and features with Streamlit

---

## 📦 Technologies Used

### Core
- Python 3.10+
- uv (environment & dependency manager)
- pyproject.toml + uv.lock
- Kafka (streaming)
- FastAPI (microservices)
- Streamlit (visualization)
- Docker / Docker Compose

### ML
- scikit-learn / XGBoost / LightGBM
- pandas, numpy
- MLflow (experiment tracking & model registry)

### DevOps / MLOps
- Docker
- Makefile
- Prometheus + Grafana (monitoring)
- Kubernetes (optional future deployment)

---

## 🗂 Project Structure

