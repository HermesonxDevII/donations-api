# 🐍 Atividade Parcial (Técnica de Integração de Sistemas) - API de Doações 🎶

Projeto desenvolvido em **Python** e **FastAPI**.

---

## 📦 Instalação e Configuração

### ✅ Clonar o repositório
```bash
git clone https://github.com/HermesonxDevII/donations-api
cd donations-api
```

### ✅ Criar ambiente virtual
```bash
python -m venv venv
```

## ✅ Acessar ambiente virtual

#### ✅ Windows
```bash
venv\Scripts\activate
```

#### ✅ Linux/Mac
```bash
source venv/bin/activate
```

### ✅ Instalar dependências
```bash
pip install -r requirements.txt
```

### ✅ Configurando variáveis de ambiente

- Após os passos acima abra o projeto no vs code para editar as variáveis de ambiente, se ja estiver no diretorio dele no terminal basta digitar `code .` que o projeto sera aberto.

- Dentro do projeto basta editar o nome do arquivo `.env.exmaple` para `.env` e preencher as variáveis de la que são essas abaixo.

```bash
DATABASE_URL=
TEST_DATABASE_URL=
AUTH_SECRET_KEY=
AUTH_ALGORITHM=
```

- As variáveis de banco (`DATABASE_URL` e `TEST_DATABASE_URL`) não são obrigatorias pois ja esta configurado como padrão para usar sqlite na aplicação, mas se quiser usar outro banco coloque o `DSN` dele nessas duas variáveis.

- Para gerar sua `AUTH_SECRET_KEY` para digitar no terminal o comando abaixo, e copiar e colar o resultado dele na variavel.

```bash
python generate_secret.py
```

- E sobre o `AUTH_ALGORITHM` você pode usar o que quiser, por padrão usamos `HS256`.

### ✅ Executar aplicação
```bash
uvicorn src.main:app --reload
```

---

## 👩‍💻 Atribuição de funções:
| Nome                                     | Matricula  | Função                     |
| ---------------------------------------- | ---------- | -------------------------- |
| [Francisco Hermeson O. dos Santos]       | [2326241]  | Desenvolvedor(a)           |
| [Maria Joselene da Costa C. de Barcelos] | [2314797]  | Desenvolvedor(a)           |
| [Francisco Clay Oliveira]                | [2317574]  | Documentação               | 
| [Francisco Tayson Araujo santos]         | [2323799]  | Testes                     | 
| [Leonardo Estevão Silva Dos Santos]      | [2315238]  | Testes                     | 

---

## 📚 Documentação de Rotas
- 🗂️ [Arquitetura](docs/architecture.md)
- 🔐 [Authenticação](docs/authentication.md)
- 🏢 [Empresas](docs/companies.md)
- 🏫 [Instituições](docs/institutions.md)
- 🎁 [Doações](docs/donations.md)

---

## 📥 Coleção Postman

Na raiz do projeto existe uma pasta chamada **`/postman`** contendo a coleção completa de requisições para facilitar os testes da API.

---

## 🐳 Tecnologias Utilizadas

- Python
- FastAPI

---

## 🤝 Contribuição
- [HermesonSantos](https://github.com/HermesonxDevII)
- [Maria Joselene](https://github.com/j0selene)