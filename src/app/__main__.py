from fastapi import FastAPI
from engine.main_engine import main
app = FastAPI()


@app.get()
def index():
    resp = main ()
    return {'Hello':'word!', "Resp":f"{resp}"}