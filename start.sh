#!/bin/bash
set -e

# Start Celery worker
# celery -A EchoReferral.celery worker --pool=solo -l info

# Start Django development server
exec "gunicorn --bind 0.0.0.0:8000 EchoReferral.wsgi.app"
