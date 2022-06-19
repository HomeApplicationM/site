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
