FROM python:3.9
ENV APP_HOME /app
WORKDIR $APP_HOME
RUN apt-get update
RUN apt-get install -y libgl1-mesa-dev
COPY . .
CMD ["python3" , "app.py" ]