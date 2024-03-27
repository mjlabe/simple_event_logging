#!/bin/bash

# Apply migrations
python manage.py migrate

# Run the application as intended
exec "$@"
