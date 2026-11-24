# Kasir Web: Restaurant Cashier App

A responsive cashier web app built with Flask for a restaurant serving traditional Balinese dishes.

## Features
- Select menu items with quantity steppers and a live running estimate
- Optional 30% birthday voucher
- Receipt-style bill with item breakdown, total, discount, and amount due
- Responsive layout for phones and desktops

## Tech Stack
- Python, Flask
- HTML, CSS, vanilla JavaScript

## Run Locally
```bash
git clone https://github.com/FilaFadilla/kasirV2.git
cd kasirV2
pip install -r requirements.txt
python app.py
```
Then open http://127.0.0.1:5000 in your browser.

## Project Structure
- `app.py`: Flask routes
- `kasir_logic.py`: prices and calculation logic
- `templates/`: `index.html` (order page), `bill.html` (receipt)
- `static/style.css`: styling

## Screenshots
Add screenshots of the order page and the bill here.
