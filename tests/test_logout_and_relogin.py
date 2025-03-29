def test_logout_and_relogin(auth_service):
    username = "valid_user"
    assert auth_service.login(username, "CorrectPassword!") == "Login bem-sucedido."
    auth_service.unlock_user(username)  # Simula logout
    assert auth_service.login(username, "WrongPassword") == "Senha incorreta."

def test_sql_injection(auth_service):
    assert auth_service.login("valid_user", "' OR '1'='1") == "Senha incorreta."
    assert auth_service.login("' OR '1'='1", "CorrectPassword!") == "Usuário não encontrado."

def test_case_sensitivity(auth_service):
    assert auth_service.login("User123", "CorrectPassword!") == "Usuário não encontrado."
    assert auth_service.login("user123", "CorrectPassword!") == "Usuário não encontrado."