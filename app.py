import uvicorn
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware

from dashapp import create_dash_app

app = FastAPI()


@app.get("/")
def read_main():
    return {
        "routes": [
            {"method": "GET", "path": "/", "summary": "Landing"},
            {"method": "GET", "path": "/status", "summary": "App status"},
            {"method": "GET", "path": "/dash", "summary": "Sub-mounted Dash application"},
        ]
    }


@app.get("/status")
def get_status():
    return {"status": "ok"}


app.mount("/", WSGIMiddleware(create_dash_app().server))


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
