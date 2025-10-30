* criar um model 
```
from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    deadline = models.DateTimeField(null=True, blank=True)
    finished_at = models.DateTimeField(null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

* rodar o migrate
```
python manage.py migrate
```

* rodando o make
```
python manage.py makemigrations
```

* rodar o migrate novamente
```
python manage.py migrate
```