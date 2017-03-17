FROM python:2.7.13
MAINTAINER dharmishadoshi "dharmishadoshi@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "app.py"]
CMD ["https://github.com/dharmisha/assignment1-config-example"]