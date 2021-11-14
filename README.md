# simple-fastAPI-webapp
Use fastAPI to generate web app. Docker, python and fastAPI are the core technologies. Minimalism is preferred over a shiny interface, and it must be easy to put into production.

Why [fastAPI](https://fastapi.tiangolo.com/) over flask? Read [this article](https://amitness.com/2020/06/fastapi-vs-flask/) for a detailed intro to the topic.

## Docker build and run
```
docker build -t luxapp .
docker run -p 8000:8000 -t -i luxapp
```
Then visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/). The docs are at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Development in venv
- `python3 -m venv luxenv`
- `source luxenv/bin/activate`
- `pip3 freeze >  requirements.txt`
- `uvicorn main:app --reload`
- [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
