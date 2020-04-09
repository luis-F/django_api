### Instalação
```sh
$ docker-compose build
```

### Entrar no docker
```sh
$ docker-compose run django bash
```

### Dentro do docker
```sh
# Roda as migrations
$ python manage.py makemigrations

# Aplica as alterações de fato no banco
$ python manage.py migrate
```

### Rodar
```sh
$ python manage.py runserver
```
