FROM python:3.10.11-alpine as build

WORKDIR /app/

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ./bin/entrypoint.sh .
RUN sed -i 's/\r$//g' /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

COPY . .

FROM build as test
RUN python manage.py test

FROM build as final
ENTRYPOINT [ "/app/entrypoint.sh" ]
