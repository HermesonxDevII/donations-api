def setup_donator_and_receiver(client):
    donator_user_res = client.post("/users/register", json={
        "name": "Doador Teste", "cpf": "11122233344", "email": "doador@teste.com",
        "password": "123", "user_type": 2
    })
    donator_token = donator_user_res.json()["token"]["access_token"]

    client.post(
        "/companies/",
        json={"cnpj": "11222333000144", "corporate_reason": "Empresa Doadora", "fantasy_name": "Doadora"},
        headers={"Authorization": f"Bearer {donator_token}"}
    )
    company_id = client.get("/companies/").json()[0]["id"]

    receiver_user_res = client.post("/users/register", json={
        "name": "Receptor Teste", "cpf": "55566677788", "email": "receptor@teste.com",
        "password": "123", "user_type": 3
    })
    receiver_token = receiver_user_res.json()["token"]["access_token"]

    client.post(
        "/institutions/",
        json={"cnpj": "55666777000188", "public_name": "Instituição Receptora", "mission": "Ajudar", "area_of_activity": "Comida"},
        headers={"Authorization": f"Bearer {receiver_token}"}
    )
    institution_id = client.get("/institutions/").json()[0]["id"]
    
    return donator_token, company_id, institution_id

def test_create_donation_success(client):
    donator_token, company_id, institution_id = setup_donator_and_receiver(client)
    
    response = client.post(
        "/donations/",
        json={
            "food_name": "Arroz",
            "description": "Pacote 5kg",
            "quantity": "10 pacotes",
            "expiration_date": "2026-12-31",
            "donor_id": company_id,
            "receiver_id": institution_id
        },
        headers={"Authorization": f"Bearer {donator_token}"}
    )
    
    assert response.status_code == 200
    assert response.json() == {"message": "donation created has successfully!"}

def test_create_donation_by_non_company_user_fails(client):
    user_response = client.post("/users/register", json={
        "name": "Não Doador", "cpf": "99988877766", "email": "naodoador@teste.com",
        "password": "123", "user_type": 3
    })
    token = user_response.json()["token"]["access_token"]
    
    response = client.post(
        "/donations/",
        json={
            "food_name": "Feijão", "description": "Pacote 1kg", "quantity": "5",
            "expiration_date": "2025-01-01", "donor_id": 1, "receiver_id": 1
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    
    assert response.status_code == 403
    assert response.json() == {"detail": "Only companies can register donations."}

def test_create_donation_to_nonexistent_institution_fails(client):
    donator_token, company_id, _ = setup_donator_and_receiver(client)
    
    response = client.post(
        "/donations/",
        json={
            "food_name": "Macarrão", "description": "Pacote 500g", "quantity": "20",
            "expiration_date": "2026-05-10", "donor_id": company_id, "receiver_id": 999
        },
        headers={"Authorization": f"Bearer {donator_token}"}
    )
    
    assert response.status_code == 404
    assert response.json() == {"detail": "Institution with ID 999 not found."}