import secrets

secret_key = secrets.token_hex(64)

print(f"Sua nova AUTH_SECRET_KEY é: {secret_key}")