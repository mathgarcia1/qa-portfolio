# QA Portfolio: Generic Project Manager E2E Suite

Este projeto demonstra uma suíte de testes de ponta a ponta (E2E) para uma plataforma de gestão de projetos. O objetivo é validar fluxos críticos de negócio usando **Playwright**, **Python** e o padrão **Page Object Model (POM)**.

## 🚀 Fluxos Cobertos
1. **Autenticação:** Validação de login com sucesso e tratamento de erros.
2. **Gestão de Usuários:** Criação e listagem de novos usuários no painel administrativo.
3. **Módulo de BI:** Fluxo de criação e visualização de relatórios externos integrados.
4. **Importação de Cronogramas:** Simulação de upload de arquivos XML e mapeamento de colunas dinâmicas.

## 🛠️ Decisões Técnicas
- **Page Object Model (POM):** Encapsulamento de seletores e lógica de interação para facilitar a manutenção e legibilidade.
- **Isolamento de Ambiente:** Uso de fixtures do Pytest para subir um servidor Uvicorn efêmero durante a execução dos testes.
- **CI/CD Integrado:** Workflow do GitHub Actions configurado para rodar os testes automaticamente em cada push.
- **Segurança de Dados:** Uso de variáveis de ambiente para credenciais de teste, evitando vazamento de segredos.

## 📦 Como Executar

### Via Docker
```bash
docker-compose up --build
```

### Localmente
1. Instale as dependências: `pip install -r requirements.txt`
2. Instale o Playwright: `playwright install chromium`
3. Execute os testes: `pytest qa-portfolio/tests`

---
*Este é um projeto de demonstração técnica focado em qualidade de software.*
