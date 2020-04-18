### Instalação
```sh
$ docker-compose build
```

### Entrar no docker
```sh
$ docker-compose run django /bin/sh
```

### Dentro do docker
```sh
# Roda as migrations
$ python manage.py makemigrations

# Aplica as alterações de fato no banco
$ python manage.py migrate

# Criar superuser para gerenciamento
$ python manage.py createsuperuser

# Adiciona dados iniciais no banco
$ python manage.py loaddata stocks

# Para rodar o linter
$ pylint --load-plugins pylint_django ./stock ./config/ ./daily_historical/
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

### Unit test
```sh
# dentro do container
$ coverage run manage.py test -v 2

# Para ver o quanto do código em si foi testado
$ coverage report
```

### Formato request.post
```sh
#Stock
{
    "symbol": "PETR4.SA"
}

#Daily historical
{
    "stockId": 1,
    "date": '2020-04-14',
    "open": 17.02,
    "high": 17.3,
    "low": 16.61,
    "close": 16.73,
    "volume": 91017200.0,
    "dividends": 0.0,
    "stockSplits": 0.0
}

#multiples daily historical
[{
    "stockId": 1,
    "date": "2020-04-09",
    "open": 17.94,
    "high": 18.69,
    "low": 16.5,
    "close": 16.82,
    "volume": 185771300.0,
    "dividends": 0.0,
    "stockSplits": 0.0
},
{
    "stockId": 1,
    "date": '2020-04-14',
    "open": 17.02,
    "high": 17.3,
    "low": 16.61,
    "close": 16.73,
    "volume": 91017200.0,
    "dividends": 0.0,
    "stockSplits": 0.0
}]

```
