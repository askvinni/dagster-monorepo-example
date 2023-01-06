FROM python:3.9.9-slim AS venv

RUN apt-get update && apt-get upgrade -yqq
RUN apt-get install git libpq-dev -y

RUN pip install poetry
ENV PATH /root/.poetry/bin:$PATH

WORKDIR /app/project
COPY some-dagster-project/pyproject.toml some-dagster-project/poetry.lock ./
COPY dagster-utils ../dagster-utils
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

# The `--copies` option tells `venv` to copy libs and binaries
# instead of using links (which could break since we will
# extract the virtualenv from this image)
RUN python -m venv --copies /app/venv
RUN . /app/venv/bin/activate && pip install -r requirements.txt

FROM python:3.9.9-slim as main
RUN mkdir -p /opt/dagster/dagster_home/
WORKDIR /opt/dagster/dagster_home/

COPY --from=venv /app/venv /app/venv/
COPY --from=venv /app/dagster-utils /app/dagster-utils
ENV PATH /app/venv/bin:$PATH

COPY some-dagster-project/. .

EXPOSE 4266