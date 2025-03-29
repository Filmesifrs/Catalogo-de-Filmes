import time
from auth_service import AuthService

def test_login_response_time(auth_service):
    start_time = time.time()
    auth_service.login("valid_user", "CorrectPassword!")
    response_time = time.time() - start_time
    assert response_time <= AuthService.MAX_RESPONSE_TIME, "Erro: Tempo de resposta excedido."