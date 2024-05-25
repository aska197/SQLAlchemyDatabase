# SQLAlchemy Database Project

## Overview

This project implements a database system using SQLAlchemy to manage data for a school, including students, groups, teachers, subjects, and grades. The project demonstrates how to design database schemas, handle migrations, seed data with random values, and perform complex queries. The entire setup is managed through Python scripts, utilizing Alembic for migrations and Faker for data generation.

## Installation

1. Clone the repository:
2. Install the required Python packages:
3. Set up your database configuration in `config.ini`.

## Usage

### Step 1: Define Models
Define the models for students, groups, teachers, subjects, and grades in `models.py`.

### Step 2: Database Migrations
Use Alembic for database migrations. Initialize Alembic and create migrations.

### Step 3: Seed Database
Use the `seed.py` script to populate the database with random data using Faker.

### Step 4: Execute Queries
Perform complex queries using SQLAlchemy in `my_select.py`. Define functions for various queries:

## Conclusion

This project showcases how to use SQLAlchemy for database modeling, Alembic for migrations, Faker for data seeding, and performing complex queries with SQLAlchemy's ORM capabilities. The setup and scripts provide a complete pipeline for database creation, management, and data retrieval.
