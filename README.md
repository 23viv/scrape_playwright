## Overview

This project is a **web scraper built with Python and Playwright** that extracts company information from the VTU Internship Portal.

The scraper automatically navigates through **all company listing pages (1–72)** on the VTU website and collects detailed information about each company.

The extracted data is saved into a **CSV dataset** for further analysis or processing.

---

# Features

* Crawls **72 pages of company listings**
* Visits each company profile page
* Extracts structured company information
* Handles duplicates and errors gracefully
* Saves results into a clean **CSV dataset**

---

# Data Collected

The scraper extracts the following fields:

| Field        | Description                    |
| ------------ | ------------------------------ |
| name         | Name of the company            |
| domain       | Industry domain of the company |
| company_size | Number of employees            |
| location     | City, state, and country       |
| year_founded | Year the company was founded   |
| website      | Official company website       |


---

# Technologies Used

* Python 3
* Playwright
* CSV module
* Web scraping techniques
* Dynamic page handling

---
# Installation

## 1. Clone the repository

```bash
git clone https://github.com/yourusername/vtu-company-scraper.git
cd vtu-company-scraper
```

## 2. Install dependencies

```bash
pip install playwright
```

Install browser drivers:

```bash
playwright install
```

---

# Usage

Run the scraper using:

```bash
python scape.py
```

The script will:

1. Visit all **72 company listing pages**
2. Collect company profile links
3. Extract company information
4. Save the results to:

```
companies.csv
```

---

# Project Structure

```
project/
│
├── scape.py
├── companies.csv
└── README.md
```

---
# Disclaimer

This project is intended for **educational and research purposes only**.

Always respect a website's **robots.txt**, terms of service, and scraping policies.

---

