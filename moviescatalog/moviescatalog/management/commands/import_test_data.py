import os
from django.core.management.base import BaseCommand
from django.db import connection
from django.conf import settings
import sqlparse  # pip install sqlparse

class Command(BaseCommand):
  help = 'Executa SQL fixo em tests/data/moviescatalog.sql (na raiz do projeto)'

  def handle(self, *args, **options):
    sql_path = os.path.abspath(os.path.join(settings.BASE_DIR, '..', 'tests', 'data', 'moviescatalog.sql'))

    if not os.path.isfile(sql_path):
      self.stderr.write(self.style.ERROR(f'Arquivo SQL não encontrado: {sql_path}'))
      return

    with open(sql_path, 'r', encoding='utf-8') as f:
      sql = f.read()

    # Usa sqlparse para dividir corretamente os statements SQL
    statements = sqlparse.split(sql)

    with connection.cursor() as cursor:
      for statement in statements:
        statement = statement.strip()
        if not statement:
          continue

        try:
          cursor.execute(statement)
        except Exception as e:
          self.stderr.write(self.style.ERROR(f'Erro ao executar: {statement[:80]}...'))
          self.stderr.write(self.style.ERROR(str(e)))

    self.stdout.write(self.style.SUCCESS('SQL executado com sucesso!'))
