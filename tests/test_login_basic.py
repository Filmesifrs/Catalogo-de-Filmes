import pytest

@pytest.mark.parametrize("username, password, expected_message", [
    ("valid_user", "WrongPassword", "Senha incorreta."),
    ("invalid_user", "CorrectPassword!", "Usuário não encontrado."),
    ("invalid_user", "WrongPassword", "Usuário não encontrado."),
    ("valid_user", "CorrectPassword!", "Login bem-sucedido."),
    ("", "", "Usuário e senha são obrigatórios."),
    ("", "somepassword", "Usuário e senha são obrigatórios."),
    ("valid_user", "", "Usuário e senha são obrigatórios."),
    ("VALID_USER", "CorrectPassword!", "Usuário não encontrado."),
    ("valid_user", "@dm1nP@ss!", "Senha incorreta."),
    ("valid_user", "senhaErrada!", "Senha incorreta."),
    ("test_user", "p@ssw0rd", "Usuário não encontrado."),
])

def test_login_basic(username, password, expected_message, auth_service):
    assert auth_service.login(username, password) == expected_message