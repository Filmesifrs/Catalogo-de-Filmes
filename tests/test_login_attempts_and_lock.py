import time
from auth_service import AuthService

def test_login_attempts_and_lock(auth_service):
    username = "valid_user"

    for attempt in range(AuthService.MAX_ATTEMPTS):
        assert auth_service.login(username, "WrongPassword") == "Senha incorreta."

    assert "Usuário bloqueado" in auth_service.login(username, "WrongPassword")

    # Simular espera para desbloqueio
    time.sleep(AuthService.LOCK_DURATIONS[0] + 1)
    assert auth_service.login(username, "CorrectPassword!") == "Login bem-sucedido."


def test_progressive_locking(auth_service):
    username = "valid_user"

    for i in range(4):  # Simulando múltiplos bloqueios progressivos
        for attempt in range(AuthService.MAX_ATTEMPTS):
            assert auth_service.login(username, "WrongPassword") == "Senha incorreta."
        assert "Usuário bloqueado" in auth_service.login(username, "WrongPassword")
        time.sleep(AuthService.LOCK_DURATIONS[min(i, len(AuthService.LOCK_DURATIONS) - 1)] + 1)
        assert auth_service.login(username, "CorrectPassword!") == "Login bem-sucedido."
