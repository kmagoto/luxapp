# simple-fastAPI-webapp
Use fastAPI to generate web app. Docker, python and fastAPI are the core technologies. Minimalism is preferred over a shiny interface, and it must be easy to put into production.

Why [fastAPI](https://fastapi.tiangolo.com/) over flask? Read [this article](https://amitness.com/2020/06/fastapi-vs-flask/) for a detailed intro to the topic, but for me the big advantages are built in type validation, auto generated docs, and less boilerplate.

## Docker build and run
```
docker build -t webapp .
docker run -p 8000:8000 webapp:latest
```
Then visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/). The docs are at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Development in venv
- `python3.7 -m venv venv`
- `source venv/bin/activate`
- `pip3 install -r requirements.txt`
- `uvicorn main:app --reload`
- [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
