from urllib.request import Request

from fastapi import FastAPI
from calculadora import Calculadora

app = FastAPI()
calc = Calculadora()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/sumar/")
async def sumar(num1: int, num2: int):
    return {calc.sumar(num1, num2)}

@app.get("/restar/")
async def restar(num1: int, num2: int):
    return {calc.sumar(num1, num2)}

@app.get("/multiplicar/")
async def multiplicar(num1: int, num2: int):
    return {calc.sumar(num1, num2)}

@app.get("/dividir/")
async def dividir(num1: int, num2: int):
    return {calc.sumar(num1, num2)}