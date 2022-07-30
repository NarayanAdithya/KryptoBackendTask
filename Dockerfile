# start by pulling the python image
FROM python:3.8.13-slim-buster

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip3 install -r requirements.txt

# copy every content from the local file to the image
COPY ./Krypto.py /app
COPY ./config.py /app/
COPY ./entrypoint.sh /app/entrypoint.sh
COPY /app /app/app
# configure the container to run in an executed manner
ENV FLASK_APP Krypto.py

RUN flask db init
RUN flask db migrate
RUN flask db upgrade

ENTRYPOINT ["./entrypoint.sh"]

EXPOSE 8000

CMD ["python","Krypto.py" ]