# Calculadora - Code Design & Arquitetura

Bem-vindo ao projeto **Calculadora**, desenvolvido como parte do Módulo 04 da Formação Python pela **Rocketseat**. Este projeto foca em aplicar as melhores práticas de **Code Design** e **Arquitetura de Software**.

Apesar de ser uma aplicação teoricamente simples (uma calculadora), o principal objetivo deste repositório é demonstrar como estruturar um código escalável, limpo e bem arquitetado em Python.

---

## 🎯 Objetivos do Projeto

- **Arquitetura em Camadas:** Separação clara de responsabilidades (calculators, drivers, controllers, errors).
- **Tratamento de Exceções Baseado em Tipagem:** Controllers específicos para lidar de forma consistente com dados e retornos HTTP.
- **Injeção de Dependência e Desacoplamento:** Garantindo testabilidade (Test-Driven Development - TDD/Testes Unitários com pytest).
- **Clean Code (Código Limpo):** Aplicação de boas práticas focando na legibilidade, manutenibilidade e padrão de nomenclatura claro de funções e variáveis.

## 📁 Estrutura de Diretórios

A estrutura do projeto foi pensada para isolar a lógica de negócio de infraestruturas (como integrações externas, banco de dados ou framework web). A organização principal concentra-se na pasta `src/`:

```text
📦 CodeDesign
 ┣ 📂 src
 ┃ ┣ 📂 calculators      # Lógica de negócio e execução dos cálculos (Calculators 1, 2 e 3) e testes unitários
 ┃ ┣ 📂 drivers          # Integrações, interfaces e lógicas auxiliares (ex: conectores externos e APIs)
 ┃ ┣ 📂 errors           # Controladores e handlers centralizados para tratamento de exceções
 ┃ ┗ 📂 main             # Ponto de entrada, configuração das rotas e inicialização (e.g. Flask/FastAPI routes)
 ┣ 📜 run.py             # Arquivo principal para inicialização da aplicação
 ┣ 📜 README.md          # Documentação do projeto
 ┣ 📜 interface_raw.py   # Exemplificações e testes rasos de interfaces
 ┗ 📜 requirements.txt   # Dependências do projeto (libs/frameworks)
```

## 🛠️ Tecnologias e Ferramentas

- **Linguagem:** Python
- **Testes Unitários:** Pytest (Testes de métodos matemáticos e comportamentos dos controllers).
- **Framework Web (APIs):** Arquitetura desenhada e preparada para integrar com APIs via requests nas rotas (main/routes) para chamadas das lógicas contidas em *calculators*.

## 🚀 Como Executar o Projeto

### Pré-requisitos
- Python instalado em sua máquina.

### Passos

1. **Clone o repositório:**
   ```bash
   git clone <url-do-repositorio>
   ```
2. **Navegue até a pasta do projeto:**
   ```bash
   cd CodeDesign
   ```
3. **Crie e ative o ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv venv
   # No Windows (PowerShell/CMD):
   venv\Scripts\activate
   # No Mac/Linux:
   source venv/bin/activate
   ```
4. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Execute a aplicação principal:**
   ```bash
   python run.py
   ```

### 🧪 Executando os Testes

Para validar a integridade dos módulos e as lógicas de negócio:

```bash
pytest src/calculators/
```

## 🧠 Aprendizados e Conceitos Focados

- **Boas Práticas e Arquitetura:** O repositório foge dos scripts rasos ("Spaghetti Code") e visa implementações sustentáveis prontas para escala no ambiente corporativo (SOLID, Separation of Concerns).
- **Mocks & Testes:** Trabalhar com injeção de dependências (Mock Requests e Flask requests), garantindo que os calculadores sejam agnósticos à tecnologia da API.

---

<p align="center">
  <i>Desenvolvido durante a Formação Python da <b>Rocketseat</b>.</i>
</p>
