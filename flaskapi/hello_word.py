#python
from turtle import st
from typing import Optional
from unittest.util import _MAX_LENGTH
#pydantic
from pydantic import BaseModel
#fast api
from fastapi import FastAPI, Query
from fastapi import Body

app = FastAPI()
#models 
class Person(BaseModel):
	first_name :str
	last_name :str
	age :int 
	hair_color: Optional[str]=None
	is_married: Optional[bool]=None

@app.get('/')
def home():
	return (1)
#request and response body
@app.post("/person/new")
def create_person(person: Person=Body(...)):
	
	return person
#validations : query parameters
	
@app.get('/person/detail')
def show_person(name: Optional[str]= Query(None, min_length=1,max_length=50),
				age: Optional[str]=Query(None,min_length=0,max_length=3) ):
				return{name*2:age*2}