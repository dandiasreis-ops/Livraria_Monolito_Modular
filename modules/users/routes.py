"""Blueprint reservado para futuras rotas de usuários e perfis."""
from flask import Blueprint
users_bp = Blueprint("users", __name__, url_prefix="/usuarios")

@users_bp.get("/health")
def health():
    return {"status": "ok", "module": "users"}
