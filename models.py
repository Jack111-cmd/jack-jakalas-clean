from app import db
from datetime import datetime

class Signal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10))
    type = db.Column(db.String(20))
    strength = db.Column(db.Float)
    received_at = db.Column(db.DateTime, default=datetime.utcnow)

class Trade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10))
    lot_size = db.Column(db.Float)
    direction = db.Column(db.String(10))
    signal_source = db.Column(db.String(50))
    status = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)