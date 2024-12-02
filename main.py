from src.controllers.sistema import main
from src.models.plano_contrato import PlanoContrato

if __name__ == "__main__":
    planos = [
        PlanoContrato("Mensal", 199.00, 1),
        PlanoContrato("Trimestral", 179.90, 3),
        PlanoContrato("Anual", 149.90, 12)
    ]
    main(planos)
