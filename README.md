# Sales Data Engineering ETL Pipeline

An end-to-end data engineering pipeline that extracts, transforms, validates, and loads sales data using Python, Pandas, and PostgreSQL.

## Tech Stack
Python · Pandas · PostgreSQL · SQL · Git

## Key Features
- CSV data extraction and processing
- Bronze, Silver, and Gold data layers
- Data cleaning and quality validation
- PostgreSQL data loading
- SQL-based sales analysis and aggregation

## Pipeline
`CSV → Extract → Bronze → Transform → Silver → PostgreSQL → Gold`

## Project Structure
- `data/` – Source CSV files
- `src/` – ETL and validation scripts
- `bronze/` – Raw data
- `silver/` – Cleaned data
- `gold/` – Business-ready datasets
