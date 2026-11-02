"""Blueprint reservado para evolução das reservas."""
from flask import Blueprint
reservations_bp = Blueprint("reservations", __name__, url_prefix="/reservas")

@reservations_bp.get("/health")
def health():
    return {"status": "ok", "module": "reservations"}
