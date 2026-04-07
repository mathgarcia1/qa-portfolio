# 🏗️ QA Portfolio: Platform Project Management (E2E & API Suite)

[![E2E Tests](https://github.com/mathgarcia1/qa-portfolio/actions/workflows/main.yml/badge.svg)](https://github.com/mathgarcia1/qa-portfolio/actions/workflows/main.yml)

[![AllureReport](https://img.shields.io/badge/Allure_Report-View_Results-brightgreen?style=flat-square&logo=allure)](https://mathgarcia1.github.io/qa-portfolio/)

[![HitCount](https://hits.dwyl.com/matheusgarcia1/qa-portfolio.svg?style=flat-square)](http://hits.dwyl.com/matheusgarcia1/qa-portfolio)

Este projeto demonstra uma arquitetura de testes híbrida de alta performance para uma plataforma de gestão de projetos. O foco principal é a **observabilidade**, **manutenibilidade** e o conceito de **Shift-Left Testing**.

---

## 🎯 Objetivos Estratégicos
- **Cobertura Híbrida:** Validação de fluxos críticos via UI (E2E) e regras de negócio via API (Integração).
- **Estratégia Shift-Left:** Detecção precoce de vulnerabilidades de segurança e falhas lógicas na camada de serviço.
- **Dados Realistas:** Implementação da biblioteca `Faker` para geração de massa de dados dinâmica e resiliente.

## 🛠️ Stack Tecnológica & Decisões
- **[Playwright](https://playwright.dev/):** Escolhido pela velocidade de execução e auto-waiting nativo, reduzindo *flakiness*.
- **[Pytest](https://docs.pytest.org/):** Framework robusto para orquestração de testes e uso de fixtures efêmeras.
- **Page Object Model (POM):** Abstração de seletores e lógica de interação para facilitar a manutenção a longo prazo.
- **[Allure Report](https://docs.qameta.io/allure/):** Dashboard de alta fidelidade com evidências visuais e histórico de execuções.
- **FastAPI TestClient:** Validação de endpoints sem a sobrecarga de um navegador, seguindo a Pirâmide de Testes.

## 🚀 Fluxos Cobertos
1. **Autenticação Segura:** Validação de cookies JWT e tratamento de credenciais inválidas.
2. **Gestão Administrativa:** CRUD de usuários e permissões de acesso (com análise de vulnerabilidades).
3. **Módulo de BI:** Integração de relatórios externos e renderização dinâmica.
4. **Importação de Cronogramas:** Fluxo de upload de arquivos XML com mapeamento dinâmico de colunas e tratamento de erros de input.

## 📊 Observabilidade (Allure Report)
Os resultados dos testes são publicados automaticamente no GitHub Pages após cada commit.
> [Clique aqui para visualizar o último Relatório de Testes](https://mathgarcia1.github.io/qa-portfolio/)

## 📦 Como Executar

### Pré-requisitos
- Python 3.10+
- Docker & Docker-Compose (opcional)

### Localmente
1. Instale as dependências: `pip install -r requirements.txt`
2. Instale os drivers do Playwright: `playwright install chromium`
3. Execute a suíte completa com relatório:
   ```bash
   pytest tests/ --alluredir=allure-results
   ```
4. Visualize o relatório localmente:
   ```bash
   allure serve allure-results
   ```

### Via Docker
```bash
docker-compose up --build
```

---
*Este é um projeto de demonstração técnica focado em qualidade de software.*
