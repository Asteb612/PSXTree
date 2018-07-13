# Simple configuration file

type = "psql"

host = "localhost"

port = 5432

commit_strategy = "auto-forced"

layers = {
    "l1": [
        {'left-src': 'psql:groudon.simple.A', 'right-src':'psql:groudon.simple.B'}
    ]
}
