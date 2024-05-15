FROM python:3.12.3-slim-bullseye
WORKDIR /app

RUN pip install flask && pip install flask-sqlalchemy --only-binary=:all: && pip install openai && pip install semantic-kernel==0.9.5b1 && pip install 'flask[async]'

COPY . .

CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0"]