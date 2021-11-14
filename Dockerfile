FROM python:3.9.7
COPY . .
COPY ./requirements.txt ./requirements.txt
WORKDIR .

EXPOSE 8000:8000
RUN pip install -r requirements.txt
CMD [ "uvicorn", "server:app", "--host", "0.0.0.0", "--reload"]