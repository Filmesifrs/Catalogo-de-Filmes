import time
from conftest import get_db_connection
from psycopg2 import sql

class AuthService:
    LOCK_DURATIONS = [30, 60, 90, 180]  # Progressão dos bloqueios
    MAX_ATTEMPTS = 3
    MAX_RESPONSE_TIME = 5  # Tempo máximo de resposta permitido

    def __init__(self):
        self.locked_users = {}
        self.failed_attempts = {}

    def is_locked(self, username):
        return username in self.locked_users and time.time() < self.locked_users[username]

    def lock_user(self, username, attempt):
        lock_time = self.LOCK_DURATIONS[min(attempt - self.MAX_ATTEMPTS, len(self.LOCK_DURATIONS) - 1)]
        self.locked_users[username] = time.time() + lock_time

    def login(self, username, password):
        start_time = time.time()

        if not username or not password:
            return "Usuário e senha são obrigatórios."

        if self.is_locked(username):
            return "Usuário bloqueado. Tente novamente mais tarde."

        conn = get_db_connection()
        cursor = conn.cursor()
        query = sql.SQL("SELECT password FROM users WHERE username = %s")
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()

        if not result:
            return "Usuário não encontrado."

        if result[0] != password:
            self.failed_attempts[username] = self.failed_attempts.get(username, 0) + 1
            if self.failed_attempts[username] >= self.MAX_ATTEMPTS:
                self.lock_user(username, self.failed_attempts[username])
            return "Senha incorreta."

        self.failed_attempts.pop(username, None)  # Reseta tentativas ao sucesso
        response_time = time.time() - start_time

        if response_time > self.MAX_RESPONSE_TIME:
            return "Erro: Tempo de resposta excedido."

        return "Login bem-sucedido."

    def unlock_user(self, username):
        self.locked_users.pop(username, None)


auth_service = AuthService()
