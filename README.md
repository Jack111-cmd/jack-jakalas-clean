# Jack Jakalas

Self-hosted trading signal and execution backend using Flask + MetaTrader.

## Setup

1. Install dependencies:
   pip install -r requirements.txt

2. Initialize DB:
   flask shell
   >>> from app import db
   >>> db.create_all()

3. Run:
   python run.py