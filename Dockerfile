FROM python:3.13
# set work directory
WORKDIR /usr/src/app/
# copy project
COPY . /usr/src/app/
# install dependencies
RUN pip install pytelegrambotapi
RUN pip install sqlalchemy
# run app
CMD ["python", "main.py"]