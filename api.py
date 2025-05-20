from flask import Blueprint, request, jsonify
from app.models import db, Trade, Signal

api_bp = Blueprint("api", __name__)

@api_bp.route("/signal", methods=["POST"])
def receive_signal():
    data = request.json
    signal = Signal(
        symbol=data.get("symbol"),
        type=data.get("type"),
        strength=data.get("strength")
    )
    db.session.add(signal)
    db.session.commit()
    return jsonify({"status": "signal received"})

@api_bp.route("/trade", methods=["POST"])
def place_trade():
    data = request.json
    trade = Trade(
        symbol=data.get("symbol"),
        lot_size=data.get("lot_size"),
        direction=data.get("direction"),
        signal_source=data.get("signal_source"),
        status="pending"
    )
    db.session.add(trade)
    db.session.commit()
    return jsonify({"status": "trade created", "id": trade.id})