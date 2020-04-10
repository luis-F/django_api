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

# Criar superuser para gerenciamento
$ python manage.py createsuperuser
```

### Testar funcionamento
```sh
# fora do container
$ docker-compose up

# acessar no navegador
$ docker_ip:8000/api

# acessar painel de admin
docker_ip:8000/admin
```

### Formato request.post
```sh
{
    "symbol": "PETR4.SA",
    "historical_data": [
        {
            "date": "2020-04-09",
            "open": 1.6,
            "high": 2.6,
            "low": 0.6,
            "close": 1.9,
            "volume": 3000.0,
            "dividends": 0.0,
            "stock_splits": 0.0
        }
    ]
},
```
