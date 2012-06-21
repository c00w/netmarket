uwsgi --http :80  --file ../__init__.py --pythonpath ../../ --module frontend:app --processes 16
