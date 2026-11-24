# Ecommerce Data Engineering Pipeline

An end-to-end Data Engineering project built using Python, Pandas, PostgreSQL, REST APIs, Docker, and Apache Airflow.

## Project Overview

This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline for processing e-commerce order data and REST API data.

The pipeline extracts raw data, performs data cleaning and transformation, validates data quality, and loads processed records into PostgreSQL.

Apache Airflow is used to orchestrate and execute the ETL pipeline through a DAG running inside Docker containers.

## Tech Stack

- **Language:** Python
- **Data Processing:** Pandas
- **Database:** PostgreSQL
- **Database Integration:** SQLAlchemy
- **API Integration:** REST API, Requests
- **Orchestration:** Apache Airflow
- **Containerization:** Docker & Docker Compose
- **Version Control:** Git & GitHub

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
│   ├── __init__.py
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

### CSV ETL Pipeline
- Extract e-commerce order data using Pandas.
- Clean data by removing duplicates and invalid records.
- Transform product names and calculate revenue.
- Categorize orders based on their status.
- Validate data quality before loading.
- Load processed records into PostgreSQL.

### REST API Pipeline
- Extract data from REST APIs.
- Handle paginated API responses.
- Perform data cleaning and validation.
- Implement basic ID-based incremental extraction.
- Prevent duplicate records using PostgreSQL conflict handling.

### Airflow Orchestration
- Created an Apache Airflow DAG named `ecommerce_etl_pipeline`.
- Execute the existing Python ETL pipeline through an Airflow task.
- Run Airflow using Docker Compose.
- Monitor task execution and logs through the Airflow UI.

### Database Configuration
- Use environment variables for database credentials.
- Keep sensitive configuration outside Git using `.env` files.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/AvinashParab99/ecommerce-data-pipeline-airflow.git
cd ecommerce-data-pipeline-airflow
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure PostgreSQL

Create a PostgreSQL database named `ecommerce_db`.

Create a `.env` file in the project root:

```env
DB_URL=postgresql+psycopg2://postgres:YOUR_PASSWORD@localhost:5432/ecommerce_db
```

Replace `YOUR_PASSWORD` with your PostgreSQL password.

### 5. Run the CSV ETL pipeline

```bash
python -m src.pipeline
```

### 6. Run the API pipeline

```bash
python -c "from src.api_extract import extract_paginated_data, load_api_data; df = extract_paginated_data(); load_api_data(df)"
```

## Airflow Setup

Prerequisites:
- Docker Desktop
- PostgreSQL running on the host machine

Create `airflow/.env`:

```env
AIRFLOW_UID=50000
DB_URL=postgresql+psycopg2://postgres:YOUR_PASSWORD@host.docker.internal:5432/ecommerce_db
```

Start Docker Desktop and open a terminal inside the `airflow` directory.

Initialize Airflow (first-time setup):

```bash
docker compose up airflow-init
```

Start Airflow services:

```bash
docker compose up -d
```

Open the Airflow UI:

http://localhost:8080

Default local learning credentials:

- Username: `airflow`
- Password: `airflow`

Unpause and trigger the `ecommerce_etl_pipeline` DAG from the Airflow UI.

## Pipeline Execution Results

The CSV pipeline was successfully executed through Apache Airflow.

| Metric | Result |
|---|---:|
| Total extracted records | 6 |
| Rejected records | 2 |
| Cleaned records | 4 |
| Records loaded | 4 (initial load) |
| Total transformed revenue | 1,221,000 |

The PostgreSQL table was verified after execution.

The pipeline also uses conflict handling to prevent duplicate order records during subsequent runs.

## Airflow DAG Execution

The Ecommerce ETL pipeline successfully executed through Apache Airflow.

![Airflow DAG Success](screenshots/airflow-success.png)

## Learning Outcomes

- Understanding end-to-end ETL architecture.
- Working with Pandas for data processing.
- Extracting data from REST APIs.
- Implementing pagination and basic incremental extraction.
- Integrating Python applications with PostgreSQL.
- Implementing data quality validation.
- Orchestrating ETL workflows using Apache Airflow.
- Running data engineering services using Docker.
- Managing configuration using environment variables.

## Author

**Avinash Parab**

GitHub: https://github.com/AvinashParab99