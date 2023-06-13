FROM python:3.11.0
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
# RUN apt-get update
# RUN apt-get add make automake gcc g++ subversion python3-dev
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt
COPY . /app
CMD [ "python3", "app.py"]