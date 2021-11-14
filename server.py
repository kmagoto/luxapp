from fastapi import FastAPI, Form
import uvicorn

app = FastAPI()


@app.get("/")
async def read_root():
    return { "Lux app": "Welcome to Lux app"
    		###def my_function(x, y, z):
###    """
###>>> my_function(2, 3, addition)
###5
###>>> my_function(0, 5, multiplication)
###0
###    """
### return()
  

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = str(input("Select the operator you want among division, multiplication, addition, subtraction, modulus: "))

addition = x+y
multiplication = x*y
division = x/y
subtraction = x-y

if z == "addition":
    print("x added to y is: {}".format(addition))
elif z == "subtraction":
    print("x subtracted y is: {}".format(subtraction))
elif z == "division":
    print("x divided by y is: {}".format(division))
elif z == "multiplication":
    print("x multiplied by y is: {}".format(multiplication))
    		 } 

@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username, "password": password}    
 
if __name__ == "__main__":
    uvicorn.run('server:app', port=8000, reload=False)