FROM python:3.12-slim

# set directories
ENV APP_HOME=/distributed-task-scheduler \
	POETRY_NO_INTERACTION=1

# create app directory
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

RUN pip install poetry
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry install --no-root

# Copy the rest of the application code
COPY . .

# CMD ["poetry", "run", "python", "manage.py", "runserver"]
