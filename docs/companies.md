⬅️ [Voltar](../README.md)

# 🔐 Rotas de Authenticação

- Todas as rotas de authenticação tem o prefixo `/companies` antes delas.

- Essas rotas necessitam de um **token JWT** que deve ser usado no cabeçalho `Authorization` para fazer uso delas, Para mais informações consulte [Authenticação](./authentication.md).

```bash
Authorization: Bearer {token}
```

---
## 📄 Index

| Método | Endpoint    | Descrição                            |
|--------|-------------|--------------------------------------|
| GET    | `/`         | Lista todas as empresas cadastradas. |

### ⬅️ Response

```json
[
  {
    "cnpj": "string",
    "corporate_reason": "string",
    "fantasy_name": "string",
    "street": "string",
    "neighborhood": "string",
    "number": "string",
    "postal_code": "string",
    "phone": "string",
    "email": "user@example.com",
    "id": 0,
    "owner_id": 0,
    "donations_made": []
  }
]
```

---
## 👁️ View

| Método | Endpoint         | Descrição                        |
|--------|------------------|----------------------------------|
| GET    | `/{company_id}`  | Lista uma empresa em específico. |

### ⬅️ Response

```json
{
  "cnpj": "string",
  "corporate_reason": "string",
  "fantasy_name": "string",
  "street": "string",
  "neighborhood": "string",
  "number": "string",
  "postal_code": "string",
  "phone": "string",
  "email": "user@example.com",
  "id": 0,
  "owner_id": 0,
  "donations_made": []
}
```

---
## ➕ Store

| Método | Endpoint  | Descrição              |
|--------|-----------|------------------------|
| POST   | `/`       | Cria uma nova empresa. |

### ➡️ Requisição

```bash
{
  "cnpj": "string",
  "corporate_reason": "string",
  "fantasy_name": "string",
  "street": "string",
  "neighborhood": "string",
  "number": "string",
  "postal_code": "string",
  "phone": "string",
  "email": "user@example.com"
}
```

### ⬅️ Response

```json
"company created has successfully!"
```

---
## ✏️ Update

| Método | Endpoint         | Descrição                    |
|--------|------------------|------------------------------|
| PUT    | `/{company_id}`  | Edita uma empresa existente. |

### ➡️ Requisição

```bash
{
  "cnpj": "string",
  "corporate_reason": "string",
  "fantasy_name": "string",
  "street": "string",
  "neighborhood": "string",
  "number": "string",
  "postal_code": "string",
  "phone": "string",
  "email": "user@example.com"
}
```

### ⬅️ Response

```json
"company updated has successfully!"
```

---
## 🗑️ Destroy

| Método   | Endpoint         | Descrição                     |
|----------|------------------|-------------------------------|
| DELETE   | `/{company_id}`  | Delete uma empresa existente. |

### ⬅️ Response

```json
"company deleted has successfully!"
```

---
## 📚 Outras Documentações
- 🏠 [Início](../README.md)
- 🗂️ [Arquitetura](./architecture.md)
- 🔐 [Authenticação](./authentication.md)
- 🏫 [Instituições](./institutions.md)
- 🎁 [Doações](./donations.md)