#python
from enum import Enum
from typing import Optional

#pydantic
from pydantic import BaseModel
from pydantic import Field
#fast api
from fastapi import FastAPI, Path, Query
from fastapi import Body

app = FastAPI()
#models 

class Hair_color(Enum):
	white: str= "white"
	brown: str= "brown"
	redhead: str= "redhead"
	blonde: str= "white"

class Location(BaseModel):
	city:str
	state:str
	zip:int

class Person(BaseModel):
	first_name :str = Field(...,
	min_length=1,max_length=50,)
	last_name :str= Field(...,
	min_length=1,max_length=50,)
	age :int =Field(...,gt=1,le=120)
	hair_color: Optional[Hair_color]=Field(default=None)
	is_married: Optional[bool]=Field(default=None)

@app.get('/')
def home():
	return (1)
#request and response body
@app.post("/person/new")
def create_person(person: Person=Body(...)):
	
	return person
#validations : query parameters
	
@app.get('/person/detail')
def show_person(name: Optional[str]= Query(None,
	 min_length=1,max_length=50,
	title='Person Name',
	description="this is the person name. it's between 1 and 50 characters"),
	age: str=Query(...,		
		min_length=0,
		max_length=3,
		title='Person age',description='this is person age, it is bewteen 0 to 999') ):
				return{name*2:age*2}
#validaciones : Path parameters
@app.get("/person/deatil/{person_id}")
def  show_person(
	person_id: int = Path(...,
	gt=0,
	title='Person id'
	,description='this is the  uniqui person id ')
):
	return{person_id:'it exists¡'}
#validaciones : request body
@app.put("/person/{person_id}")
def update_person(
	person_id: int =Path(
		...,title="Person id",description="this is the person id",gt=0
),person: Person=Body(...),
Location: Location=Body(...)):
	output= person.dict()
	output.update(Location.dict())

	return output
