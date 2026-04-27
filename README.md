# Local Food Waste Connector

A Python + Flask web app that helps local businesses find eco-friendly alternatives to plastic products.

## What it does

- Lets a business search for products like **"plastic forks and spoons"**.
- Shows matching sustainable suppliers.
- Includes example companies like **Biofase** (Mexico), which uses avocado pits to create compostable cutlery.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open: http://127.0.0.1:5000

## Current data model

Each supplier record includes:

- Company name
- Country
- Website
- Plastic products replaced
- Alternative materials used
- Notes

You can add more suppliers in `app.py` inside the `ECO_OPTIONS` list.
