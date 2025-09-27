⬅️ [Voltar](../README.md)

# 🔐 Rotas de Authenticação

- Todas as rotas de authenticação tem o prefixo `/users` antes delas.

- Essas rotas também retornam um **token JWT** que deve ser usado no cabeçalho `Authorization`, de qualquer outro endpoint da aplicação que não seja `/register` ou `/login`, de acordo com o seu tipo de usuário, explicado mais abaixo.

```bash
Authorization: Bearer {token}
```

---
## ➕ Registro

| Método | Endpoint    | Descrição                                                    |
|--------|-------------|--------------------------------------------------------------|
| POST   | `/register` | Cria um usuário na aplicação.                                |

### ➡️ Requisição

```bash
{
  "name": "string",
  "cpf": "string",
  "email": "user@example.com",
  "password": "string",
  "user_type": 0
}
```

- **Tipos de usuário:** 1 - Admin, 2 - Dono de empresa, 3 - Dono de Instituição.

### ⬅️ Response

```json
{
  "message": "string",
  "token": {
    "access_token": "string",
    "token_type": "string"
  }
}
```

---
## 🔑 Login

| Método | Endpoint  | Descrição                                                    |
|--------|-----------|--------------------------------------------------------------|
| POST   | `/login`  | Loga um usuário na aplicação.                                |

### ➡️ Requisição

```bash
{
  "email": "user@example.com",
  "password": "string"
}
```

### ⬅️ Response

```json
{
  "message": "string",
  "token": {
    "access_token": "string",
    "token_type": "string"
  }
}
```

---
## 📚 Outras Documentações
- 🏠 [Início](../README.md)
- 🗂️ [Arquitetura](./architecture.md)
- 🏢 [Empresas](./companies.md)
- 🏫 [Instituições](./institutions.md)
- 🎁 [Doações](./donations.md)