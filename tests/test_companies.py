def test_create_company_success(client):
    user_response = client.post(
        "/users/register",
        json={
            "name": "Dono de Empresa",
            "cpf": "11122233344",
            "email": "dono@empresa.com",
            "password": "senha123",
            "user_type": 2
        }
    )
    token = user_response.json()["token"]["access_token"]
    
    company_response = client.post(
        "/companies/",
        json={
            "cnpj": "11222333000144",
            "corporate_reason": "Empresa Teste LTDA",
            "fantasy_name": "API de Teste"
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    
    assert company_response.status_code == 201
    assert company_response.json() == {"message": "company created has successfully!"}

def test_create_company_unauthorized_user_type(client):
    user_response = client.post(
        "/users/register",
        json={
            "name": "Dono de ONG",
            "cpf": "22233344455",
            "email": "dono@ong.com",
            "password": "senha123",
            "user_type": 3
        }
    )
    token = user_response.json()["token"]["access_token"]
    
    company_response = client.post(
        "/companies/",
        json={"cnpj": "22333444000155", "corporate_reason": "Falha", "fantasy_name": "Falha"},
        headers={"Authorization": f"Bearer {token}"}
    )
    
    assert company_response.status_code == 403
    assert company_response.json() == {"detail": "Only business owners can create business profiles."}

def test_create_company_duplicate_cnpj(client):
    user_response = client.post(
        "/users/register",
        json={"name": "Dono", "cpf": "33344455566", "email": "dono2@empresa.com", "password": "123", "user_type": 2}
    )
    token = user_response.json()["token"]["access_token"]

    client.post(
        "/companies/",
        json={"cnpj": "33444555000166", "corporate_reason": "Original", "fantasy_name": "Original"},
        headers={"Authorization": f"Bearer {token}"}
    )
    
    duplicate_response = client.post(
        "/companies/",
        json={"cnpj": "33444555000166", "corporate_reason": "Duplicada", "fantasy_name": "Duplicada"},
        headers={"Authorization": f"Bearer {token}"}
    )
    
    assert duplicate_response.status_code == 400
    assert duplicate_response.json() == {"detail": "There is already a company registered with this CNPJ."}

def test_list_all_companies(client):
    user_response = client.post(
        "/users/register",
        json={"name": "Dono Listagem", "cpf": "44455566677", "email": "dono_lista@empresa.com", "password": "123", "user_type": 2}
    )
    token = user_response.json()["token"]["access_token"]
    
    client.post("/companies/", json={"cnpj": "44555666000177", "corporate_reason": "Empresa A", "fantasy_name": "A"}, headers={"Authorization": f"Bearer {token}"})
    client.post("/companies/", json={"cnpj": "55666777000188", "corporate_reason": "Empresa B", "fantasy_name": "B"}, headers={"Authorization": f"Bearer {token}"})
    
    list_response = client.get("/companies/")
    
    assert list_response.status_code == 200
    data = list_response.json()
    assert len(data) == 2
    assert data[0]["fantasy_name"] == "A"
    assert data[1]["fantasy_name"] == "B"

def test_delete_own_company_success(client):
    user_response = client.post(
        "/users/register",
        json={"name": "Dono Delete", "cpf": "66677788899", "email": "dono_delete@empresa.com", "password": "123", "user_type": 2}
    )
    token = user_response.json()["token"]["access_token"]
    
    create_response = client.post(
        "/companies/",
        json={"cnpj": "66777888000199", "corporate_reason": "Para Deletar", "fantasy_name": "Deletar"},
        headers={"Authorization": f"Bearer {token}"}
    )
    company_id = client.get("/companies/").json()[0]["id"]

    delete_response = client.delete(
        f"/companies/{company_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    
    assert delete_response.status_code == 204