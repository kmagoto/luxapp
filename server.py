from fastapi import FastAPI, Form
import uvicorn

app = FastAPI()


@app.get("/")
async def read_root():
    return { from pystrich.datamatrix import DataMatrixEncoder

encoder = DataMatrixEncoder('This is a DataMatrix.')
encoder.save('./datamatrix_test.png')
print(encoder.get_ascii()) } 

@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username, "password": password}    
 
if __name__ == "__main__":
    uvicorn.run('server:app', port=8000, reload=False)