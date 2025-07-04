# 🎬 Catálogo de Filmes

O **Catálogo de Filmes** é um aplicativo web desenvolvido com **Python e Django**. Ele permite que cinéfilos organizem os filmes assistidos, registrem quantas vezes foram vistos, adicionem anotações e atribuam notas, além de consultar resumos e recomendações.

---

## 🚀 Funcionalidades

- ✅ Cadastrar filmes  
- ✅ Marcar como assistido  
- ✅ Registrar número de vezes assistido  
- ✅ Adicionar anotações  
- ✅ Atribuir notas aos filmes  
- ✅ Consultar resumos e recomendações

---

## 🛠 Tecnologias Utilizadas

- **Python 3**  
- **Django 4**  
- **MySQL**  
- **Bootstrap 5**  
- **HTML / CSS / JavaScript**

---

## 📝 Como Rodar o Projeto

### 1. Clonar o Repositório

Clone o repositório para sua máquina local:

```sh
git clone https://github.com/Filmesifrs/Catalogo-de-Filmes
cd Catalogo-de-Filmes
```

---

### 2. Criar e Ativar o Ambiente Virtual

#### Windows

Antes de tudo, verifique se seu terminal está com permissão para rodar scripts. Veja como habilitar:  
https://answers.microsoft.com/pt-br/windows/forum/all/permitir-a-execu%C3%A7%C3%A3o-de-scripts-no/f6b195cf-0be7-46e2-b88c-358c79f78343

```sh
python -m venv .venv
.venv\Scripts\activate
```

#### Linux / macOS

```sh
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3. Instalar as Dependências

Com o ambiente virtual ativado, instale as dependências:

```sh
pip install -r requirements.txt
```

---

### 4. Configuração do Banco de Dados

#### a) Criar o banco MySQL

Crie um banco de dados MySQL com o nome desejado (ex: `moviescatalog`).

#### b) Criar o arquivo `.env`

Na raiz do projeto, crie um arquivo chamado `.env` com o seguinte conteúdo:

```
DB_NAME=moviescatalog
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=3306
```

---

### 5. Aplicar as Migrações

Execute os comandos abaixo para aplicar as migrações e criar as tabelas no banco:

```sh
python manage.py migrate
```

---

### 6. Rodar o Servidor de Desenvolvimento

Inicie o servidor local do Django:

```sh
python manage.py runserver
```

Acesse no navegador:  
http://127.0.0.1:8000/

---

### 7. Criar um Superusuário (Opcional)

Para acessar o painel administrativo do Django:

```sh
python manage.py createsuperuser
```

Siga as instruções no terminal para criar seu usuário.

---

### 8. Importar Dados de Teste (Opcional)

Para importar dados de filmes para testes, execute:

```sh
python manage.py import_test_data
```

---

### 9. Adicionar as Imagens dos Filmes

Baixe o arquivo `.zip` com as imagens neste link:  
https://drive.google.com/file/d/1cY3wvEManqdWsxairHJGG4u8kPTzr1o0/view?usp=sharing

Depois, extraia o conteúdo na seguinte pasta do projeto:

```
Catalogo-de-Filmes/moviescatalog/
```

---

Pronto! Agora você pode começar a explorar e gerenciar seu catálogo de filmes! 🎥🍿