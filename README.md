# home_app

## To add a feature

In the VM, go the correct location:

```bash
cd /var/www/maizener
```

From there, run:

```bash
git checkout main
git pull
sudo systemctl stop maizener
```

If new packages have been added to requirements:

```bash
source venv/bin/activate
pip install -r requirements.txt
```

If the DB has been mutated:

```bash
flask db migrate -m "all"
flask db upgrade
```

Finally:

```bash
sudo systemctl start maizener
```

## To test in local

Install Virtual environment and dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements
```

Run the command:

```bash
uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:app
```

The app should be visible there : <http://0.0.0.0:5000/>

## Troubleshooting

Postgres issue:
Make sure postgres is running:

```bash
sudo systemctl start postgresql.service
```
