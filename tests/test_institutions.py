def test_create_institution_success(client):
    user_response = client.post(
        "/users/register",
        json={
            "name": "Dono de Instituição",
            "cpf": "11122233344",
            "email": "dono@instituicao.com",
            "password": "senha123",
            "user_type": 3
        }
    )
    token = user_response.json()["token"]["access_token"]
    
    institution_response = client.post(
        "/institutions/",
        json={
            "cnpj": "11222333000144",
            "public_name": "Instituição de Teste",
            "mission": "Ajudar o próximo",
            "area_of_activity": "Alimentação"
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    
    assert institution_response.status_code == 201
    assert institution_response.json() == {"message": "institution created has successfully!"}

def test_create_institution_unauthorized_user_type(client):
    user_response = client.post(
        "/users/register",
        json={
            "name": "Dono de Empresa",
            "cpf": "22233344455",
            "email": "dono@empresa.com",
            "password": "senha123",
            "user_type": 2
        }
    )
    token = user_response.json()["token"]["access_token"]
    
    institution_response = client.post(
        "/institutions/",
        json={"cnpj": "22333444000155", "public_name": "Falha", "mission": "Falha", "area_of_activity": "Falha"},
        headers={"Authorization": f"Bearer {token}"}
    )
    
    assert institution_response.status_code == 403
    assert institution_response.json() == {"detail": "Only institution owners can create institution profiles."}

def test_list_all_institutions(client):
    user_response = client.post(
        "/users/register",
        json={"name": "Dono Instituição", "cpf": "44455566677", "email": "dono_lista@instituicao.com", "password": "123", "user_type": 3}
    )
    token = user_response.json()["token"]["access_token"]
    
    client.post("/institutions/", json={"cnpj": "44555666000177", "public_name": "Instituição A", "mission": "A", "area_of_activity": "A"}, headers={"Authorization": f"Bearer {token}"})
    client.post("/institutions/", json={"cnpj": "55666777000188", "public_name": "Instituição B", "mission": "B", "area_of_activity": "B"}, headers={"Authorization": f"Bearer {token}"})
    
    list_response = client.get("/institutions/")
    
    assert list_response.status_code == 200
    data = list_response.json()
    assert len(data) == 2
    assert data[0]["public_name"] == "Instituição A"
    assert data[1]["public_name"] == "Instituição B"

def test_delete_own_institution_success(client):
    user_response = client.post(
        "/users/register",
        json={"name": "Dono Delete", "cpf": "66677788899", "email": "dono_delete@instituicao.com", "password": "123", "user_type": 3}
    )
    token = user_response.json()["token"]["access_token"]
    
    client.post(
        "/institutions/",
        json={"cnpj": "66777888000199", "public_name": "Para Deletar", "mission": "Deletar", "area_of_activity": "Deletar"},
        headers={"Authorization": f"Bearer {token}"}
    )
    institution_id = client.get("/institutions/").json()[0]["id"]

    delete_response = client.delete(
        f"/institutions/{institution_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    
    assert delete_response.status_code == 204