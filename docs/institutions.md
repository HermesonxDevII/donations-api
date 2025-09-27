⬅️ [Voltar](../README.md)

# 🏫 Rotas de Instituições

- Todas as rotas de instituições tem o prefixo `/institutions` antes delas.

- Essas rotas necessitam de um **token JWT** que deve ser usado no cabeçalho `Authorization` para fazer uso delas e o usuário tem que ser do tipo `3`, para mais informações consulte [Authenticação](./authentication.md).

```bash
Authorization: Bearer {token}
```

---
## 📄 Index

| Método | Endpoint    | Descrição                                |
|--------|-------------|------------------------------------------|
| GET    | `/`         | Lista todas as instituições cadastradas. |

### ⬅️ Response

```json
[
  {
    "cnpj": "string",
    "public_name": "string",
    "mission": "string",
    "area_of_activity": "string",
    "street": "string",
    "neighborhood": "string",
    "number": "string",
    "postal_code": "string",
    "phone": "string",
    "email": "user@example.com",
    "id": 0,
    "owner_id": 0,
    "donations_received": []
  }
]
```

---
## 👁️ View

| Método | Endpoint             | Descrição                            |
|--------|----------------------|--------------------------------------|
| GET    | `/{institution_id}`  | Lista uma instituição em específico. |

### ⬅️ Response

```json
{
    "cnpj": "string",
    "public_name": "string",
    "mission": "string",
    "area_of_activity": "string",
    "street": "string",
    "neighborhood": "string",
    "number": "string",
    "postal_code": "string",
    "phone": "string",
    "email": "user@example.com",
    "id": 0,
    "owner_id": 0,
    "donations_received": []
}
```

---
## ➕ Store

| Método | Endpoint  | Descrição                  |
|--------|-----------|----------------------------|
| POST   | `/`       | Cria uma nova instituição. |

### ➡️ Requisição

```bash
{
  "cnpj": "string",
  "public_name": "string",
  "mission": "string",
  "area_of_activity": "string",
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
"institution created has successfully!"
```

---
## ✏️ Update

| Método | Endpoint             | Descrição                        |
|--------|----------------------|----------------------------------|
| PUT    | `/{institution_id}`  | Edita uma instituição existente. |

### ➡️ Requisição

```bash
{
  "cnpj": "string",
  "public_name": "string",
  "mission": "string",
  "area_of_activity": "string",
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
"institution updated has successfully!"
```

---
## 🗑️ Destroy

| Método   | Endpoint             | Descrição                         |
|----------|----------------------|-----------------------------------|
| DELETE   | `/{institution_id}`  | Delete uma instituição existente. |

### ⬅️ Response

```json
"institution deleted has successfully!"
```

---
## 📚 Outras Documentações
- 🏠 [Início](../README.md)
- 🗂️ [Arquitetura](./architecture.md)
- 🔐 [Authenticação](./authentication.md)
- 🏢 [Empresas](./companies.md)
- 🎁 [Doações](./donations.md)