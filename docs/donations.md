⬅️ [Voltar](../README.md)

# 🎁 Rotas de Doações

- Todas as rotas de doações tem o prefixo `/donations` antes delas.

- Essas rotas necessitam de um **token JWT** que deve ser usado no cabeçalho `Authorization` para fazer uso delas, para mais informações consulte [Authenticação](./authentication.md).

```bash
Authorization: Bearer {token}
```

---
## ➕ Store

| Método | Endpoint  | Descrição             |
|--------|-----------|-----------------------|
| POST   | `/`       | Cria uma nova Doação. |

### ➡️ Requisição

```bash
{
  "food_name": "string",
  "description": "string",
  "quantity": "string",
  "expiration_date": "string",
  "donor_id": 0,
  "receiver_id": 0
}
```

### ⬅️ Response

```json
"donation created has successfully!"
```

---
## 📚 Outras Documentações
- 🏠 [Início](../README.md)
- 🗂️ [Arquitetura](./architecture.md)
- 🔐 [Authenticação](./authentication.md)
- 🏢 [Empresas](./companies.md)
- 🏫 [Instituições](./institutions.md)