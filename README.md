
# Ecommerce Data Engineering Pipeline

An end-to-end data engineering project built using Python, Pandas, PostgreSQL, REST APIs, and Apache Airflow.

## Project Overview

This project demonstrates how raw e-commerce data and API data can be extracted, cleaned, transformed, validated, and loaded into PostgreSQL.

## Tech Stack

- Python
- Pandas
- REST API
- PostgreSQL
- SQLAlchemy
- Apache Airflow
- Docker & Docker Compose
- Git & GitHub

## Project Structure

```text
ecommerce-data-pipeline/
├── airflow/
│   ├── dags/
│   │   └── first_dag.py
│   └── docker-compose.yaml
├── data/
│   └── raw/
│       └── orders.csv
├── src/
│   ├── extract.py
│   ├── clean.py
│   ├── transform.py
│   ├── validate.py
│   ├── load.py
│   ├── api_extract.py
│   └── pipeline.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Features

- CSV data extraction using Pandas
- Data cleaning and duplicate removal
- Data transformation and revenue calculation
- Data validation before loading
- PostgreSQL integration using SQLAlchemy
- REST API data extraction
- Paginated API extraction
- Incremental data extraction
- Duplicate prevention using SQL conflict handling
- Airflow DAG for task orchestration
- Environment variables for database credentials

## Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd ecommerce-data-pipeline
```

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure database

Create a PostgreSQL database named `ecommerce_db`.

Create a `.env` file in the project root:

```env
DB_URL=postgresql+psycopg2://postgres:YOUR_PASSWORD@localhost:5432/ecommerce_db
```

Replace `YOUR_PASSWORD` with your PostgreSQL password.

### 5. Run CSV ETL pipeline

```bash
python -m src.pipeline
```

### 6. Run API pipeline

```bash
python -c "from src.api_extract import *; df = extract_paginated_data(); load_api_data(df)"
```

## Airflow Setup

Start Docker Desktop, then navigate to the airflow folder:

```bash
cd airflow
docker compose up airflow-init
docker compose up -d
```

Open Airflow UI:

http://localhost:8080

Default local learning credentials:

- Username: airflow
- Password: airflow

Trigger `first_dag` from the Airflow UI.

## Learning Outcomes

- Understanding ETL pipeline architecture
- Working with REST APIs and pagination
- Loading data into relational databases
- Implementing basic incremental extraction
- Orchestrating tasks using Apache Airflow
- Managing database configuration securely
