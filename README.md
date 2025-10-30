#### Cria o projeto e roda

* Opcional verificar a versão do python
```
python --version
```

* 1. criar a env
```
python -m venv venv
```

* 2. ativar a env
```
venv\Scripts\activate
```

* 3. instalar o django
```
pip install django
```

* Opcional testa o django
```
django-admin
```

* 4. criar o projeto
```
django-admin startproject ecommerce .
```

* 5. rodar o projeto
```
python manage.py runserver
```

#### 6 configura o projeto

```
LANGUAGE_CODE = 'pt-br'
```

* Alterado: armazenar em UTC (USE_TZ=True) e exibir no fuso de São Paulo
```
TIME_ZONE = 'America/Sao_Paulo' 
```

#### 7 Criar uma App
python manage.py startapp todos

#### 8 configurar uma App
* ecommerce/settings.py
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todos.apps.TodosConfig',
]
```

#### Para backup

🧩 Extras importantes

Arquivo requirements.txt
Gere ele com:

pip freeze > requirements.txt


Isso permite que outras pessoas (ou servidores) recriem seu ambiente:

pip install -r requirements.txt


#### Ref.: 
```
https://www.youtube.com/watch?v=MsUL3Pgofl4
```