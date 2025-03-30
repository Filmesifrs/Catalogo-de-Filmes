
# 🎬 Catálogo de Filmes

O **Catálogo de Filmes** é um aplicativo web desenvolvido em **Python com Django** que permite aos cinéfilos organizarem os filmes assistidos, registrarem quantas vezes foram vistos, adicionarem anotações e darem notas.

## 🚀 Funcionalidades
✅ Cadastrar filmes  
✅ Marcar como assistido  
✅ Registrar quantas vezes assistiu  
✅ Adicionar anotações  
✅ Atribuir notas aos filmes  
✅ Consultar resumos e recomendações  

## 🛠 Tecnologias Utilizadas
- **Python**  
- **Django**  

## 📝 Instruções para Rodar o Projeto

### 1. **Clonar o repositório**
Primeiro, clone o repositório do projeto para o seu ambiente local:
```sh
git clone https://github.com/Danielle-Kuhn/Catalogo-de-Filmes
```

### 2. **Criar e Ativar o Ambiente Virtual**
É recomendável criar um ambiente virtual para o projeto. No terminal, navegue até a pasta do projeto e execute:

#### Para Windows:
```sh
python -m venv .venv
.venv\Scriptsctivate
```

#### Para Linux/Mac:
```sh
python3 -m venv .venv
source .venv/bin/activate
```

### 3. **Instalar as Dependências**
Com o ambiente virtual ativado, instale as dependências do projeto utilizando o `requirements.txt`:
```sh
pip install -r requirements.txt
```

### 4. **Configuração do Banco de Dados**
1. **Configuração do MySQL**: 
   - Crie um banco de dados MySQL para o projeto (caso ainda não tenha feito isso).
   
2. **Configuração do arquivo `.env`**:
   Crie um arquivo `.env` na raiz do projeto e adicione as variáveis de configuração do banco de dados. Exemplo:
   ```
   DB_NAME=moviescatalog
   DB_USER=seu_usuario
   DB_PASSWORD=sua_senha
   DB_HOST=localhost
   DB_PORT=3306
   ```

### 5. **Aplicar as Migrações**
Execute as migrações do banco de dados para criar as tabelas:
```sh
python manage.py migrate
```

### 6. **Rodar o Servidor de Desenvolvimento**
Agora, você pode rodar o servidor de desenvolvimento do Django:
```sh
python manage.py runserver
```

O servidor estará disponível em `http://127.0.0.1:8000/`.


### 7. **Criar um Superusuário (Opcional)**
Se você quiser acessar o painel administrativo do Django, crie um superusuário:
```sh
python manage.py createsuperuser
```

