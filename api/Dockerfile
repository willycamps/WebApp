FROM python:3.7.2
RUN mkdir /app
WORKDIR /app
EXPOSE 9000
COPY * /app/
RUN pip install -r requirements.txt
COPY . .
CMD [ "uwsgi", "app.ini" ]