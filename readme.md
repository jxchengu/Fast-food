...existing code...
# Fast Food

A lightweight static site and small-scripts project for exploring fast-food chains, menu items, and simple scraping/reporting.

## Quick links
- Open the site: [index.html](index.html)  
- Example pages: [mexico.html](mexico.html), [drink.html](drink.html), [chain.html](chain.html)  
- Main script (Playwright scraping): [`main.py`](main.py)  
- Core styles: [`styles.css`](styles.css), [`mexico.css`](mexico.css), [`drink.css`](drink.css), [`chain.css`](chain.css)

## Features
- Static pages describing chains, categories, and comparisons (HTML + CSS).
- Simple Playwright scraper in [`main.py`](main.py) to extract table rows from a web source.
- Lightweight, local-first content — good for learning HTML/CSS and small automation scripts.

## Requirements
- Python 3.9+ (for the included Playwright script)  
- Node.js 18+ only if you add JS tooling (not required by default)  
- Git (recommended)

## Setup & run

Python (Playwright)
1. Install Python dependencies and Playwright:
   ```sh
   python -m pip install playwright
   python -m playwright install