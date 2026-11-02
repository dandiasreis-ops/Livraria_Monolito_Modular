# Livraria — MVP em Arquitetura Monolítica Modular

Projeto acadêmico de Engenharia de Software. O sistema mantém uma única aplicação Flask, organizada em módulos com responsabilidades separadas, inspiradas no desenho de microsserviços.

## Arquitetura
- `app.py`: inicialização e composição da aplicação.
- `modules/catalog`: rotas, serviços e repositório do catálogo.
- `modules/inventory`: regra de consulta de disponibilidade.
- `modules/users`: módulo inicial (health check; funcionalidades de conta ainda não implementadas).
- `modules/reservations`: módulo inicial (health check; fluxo de reserva ainda não implementado).
- `templates/` e `static/`: interface HTML, CSS e JavaScript compartilhada.

É um **monólito modular**: os módulos são separados no código, mas executados no mesmo processo Flask e ainda utilizam dados demonstrativos em memória. Não há banco de dados persistente, autenticação real nem criação efetiva de reservas.

## Executar localmente

Requer Python 3.10 ou superior.

```bash
python -m venv .venv
```

Windows PowerShell:
```powershell
.\.venv\Scripts\Activate.ps1
```

Linux/macOS:
```bash
source .venv/bin/activate
```

Instalar dependências e iniciar:
```bash
pip install -r requirements.txt
python app.py
```

Acesse http://127.0.0.1:5000

## Endpoints
- `GET /` — catálogo com pesquisa e filtro.
- `GET /livro/<id>` — detalhes do livro.
- `GET /health` — verificação do módulo de catálogo.
- `GET /usuarios/health` — verificação do módulo de usuários.
- `GET /reservas/health` — verificação do módulo de reservas.

## Observação
Os livros e quantidades em estoque são dados fictícios para demonstração acadêmica.
