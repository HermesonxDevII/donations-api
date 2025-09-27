def test_user_registration_success(client):
    response = client.post(
        "/users/register",
        json={
            "name": "Usuário Teste",
            "cpf": "12345678901",
            "email": "teste@example.com",
            "password": "senha123",
            "user_type": 2
        }
    )
    
    assert response.status_code == 200

    data = response.json()
    assert data["message"] == "User registered has successfully!"
    assert "token" in data
    assert "access_token" in data["token"]

def test_user_registration_duplicate_email(client):
    client.post(
        "/users/register",
        json={
            "name": "Usuário Original",
            "cpf": "11122233344",
            "email": "duplicado@example.com",
            "password": "senha123",
            "user_type": 2
        }
    )
    
    response = client.post(
        "/users/register",
        json={
            "name": "Usuário Duplicado",
            "cpf": "55566677788",
            "email": "duplicado@example.com",
            "password": "outrasenha",
            "user_type": 3
        }
    )
    
    assert response.status_code == 400
    assert response.json() == {"detail": "This email is already in use."}

def test_user_login_success(client):
    user_data = {
        "name": "Usuário Login",
        "cpf": "09876543210",
        "email": "login@example.com",
        "password": "senhaforte",
        "user_type": 3
    }
    client.post("/users/register", json=user_data)
    
    response = client.post(
        "/users/login",
        json={
            "email": "login@example.com",
            "password": "senhaforte"
        }
    )
    
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "User logged has successfully!"
    assert "access_token" in data["token"]