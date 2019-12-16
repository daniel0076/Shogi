# Shogi Web

Play Shogi on web.

## Environment

+ Frontend: Angular8
+ Backend: Django Rest

## Development

### Prerequisites

Make sure the prerequisites are installed

+ python3.7 or newer
+ pipenv
+ yarn
+ npm
+ [ng-cli](https://cli.angular.io)

### Backend

install requirements

```bash
> pipenv install    # install python dependency
> pipenv run pip install channels # install channels from source
> pipenv shell  # activate virtual environment
```

Initiate Database

```bash
> cd Shogi
> python3 manage.py makemigrations Shogi_app
> python3 manage.py migrate
```

`db.sqlite3` should appear in the directory

Run backend server
```bash
python3 manage.py runserver [ip:port]
```

### Frontend

Install dependency

```bash
> cd ShogiUI
> yarn # or npm install
> npm install -g @angular/cli   # install ng cli tool
```

Run server

```bash
> ng serve
# listen on http://localhost:4200/
```

