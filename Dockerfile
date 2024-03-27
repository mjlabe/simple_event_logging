FROM python:3.12-slim-bookworm

WORKDIR /src

COPY requirements.txt /src
RUN pip install -r requirements.txt

COPY uwsgi.yaml docker-entrypoint.sh /
COPY src /src

ENTRYPOINT /docker-entrypoint.sh

# Start uWSGI
CMD ["uwsgi", "/uwsgi.yaml", "--show-config"]
