# Shogi Web

Play Shogi on web.

## Environment

+ Frontend: Angular8
+ Backend: Django Rest

## Development

### Prerequisites

+ python3.7 or newer
+ pipenv
+ yarn
+ npm
+ ng-cli

### Backend

install requirements

```
> pipenv install    # install python dependency
> pipenv shell  # activate virtual environment
```

Initiate Database

```
> cd Shogi
> python3 manage.py migrate
```

`db.sqlite3` should appear in the directory

Run backend server
```
python3 manage runserver
```

### Frontend

Install dependency

```
> cd ShogiUI
> yarn install
```

Run server

```
> ng serve
# listen on http://localhost:4200/
```

