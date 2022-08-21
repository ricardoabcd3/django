#python

from enum import Enum
from tkinter.tix import Form
from typing import Optional

#pydantic
from pydantic import AnyUrl, BaseModel, EmailStr, FilePath
from pydantic import Field, DirectoryPath
#fast api
from fastapi import FastAPI, Path, Query,Form, Header,Cookie
from fastapi import Body
from fastapi import status

app = FastAPI()
#models 
class LoginOut(BaseModel):
	usename:str =Field(...,max_length=20,min_length=3,example='user123')
	message:str =Field(default='Loging Succesfully')

class Hair_color(Enum):
	white: str= "white"
	brown: str= "brown"
	redhead: str= "redhead"
	blonde: str= "blonde"


class Location(BaseModel):
#set 26 letters beacuse the longest name plece belong Mamungkukumpurangkuntjunya Hill,Australia
#  which has 26 letters
	city:str= Field(...,max_length=26,min_length=1,)
	state:str=Field(...,max_length=26,min_length=1,)
	zip:int=Field(...,gt=1,le=10000,)
	class Config:
		schema_extra={
			"example":
			{"city": "cdmx",
			"state":"mexico",
			"zip":"55214"

			}

		}

class Person(BaseModel):
	first_name :str = Field(...,
	min_length=1,max_length=50,)
	last_name :str= Field(...,
	min_length=1,max_length=50,)
	age :int =Field(...,gt=1,le=120)
	hair_color: Optional[Hair_color]=Field(default=None)
	is_married: Optional[bool]=Field(default=None)
	email:Optional[EmailStr]=Field(default=None)
	file_path:Optional[FilePath]=Field(default=None)
	any_url:Optional[AnyUrl]=Field(default=None)

class Personbase(BaseModel):
	first_name :str = Field(...,
	min_length=1,max_length=50,)
	last_name :str= Field(...,
	min_length=1,max_length=50,)
	age :int =Field(...,gt=1,le=120)
	hair_color: Optional[Hair_color]=Field(default=None)
	is_married: Optional[bool]=Field(default=None)
	
	class Config:
		#schema_extra* required
		schema_extra ={
			#example* required
			"example":{
				"first_name": "Facundo",
				"last_name": "lopez perez",
				"age": 21,
				"hair_color":"blonde",
				"is_married":False,
				"password":"password123"			
			}
		}
class Person1(Personbase):
	password:str=Field(...,min_length=8,)
	
class Person_out(Personbase):
	pass

	




@app.get('/', status_code=status.HTTP_200_OK)
def home():
	return ("welcome to my proyect")
#request and response body
#exclude responses with model_exclude
@app.post("/person/new",response_model=Person1,response_model_exclude={'password'}
, status_code=status.HTTP_201_CREATED)
def create_person(person: Person1=Body(...)):
	
	return person
#exclude response with responses model (no valid way when you can use response model_exclude)
'''@app.post("/person/new",response_model=Person_out)
def create_person(person: Person1=Body(...)):
	
	return person'''
#validations : query parameters
	
@app.get('/person/detail', status_code=status.HTTP_200_OK)
def show_person(name: Optional[str]= Query(None,
	 min_length=1,max_length=50,
	title='Person Name',
	description="this is the person name. it's between 1 and 50 characters",example="ricardo"),
	age: str=Query(...,		
		min_length=0,
		max_length=3,
		title='Person age',description='this is person age, it is bewteen 0 to 999',example="21") ):
				return{name*2:age*2}
#validaciones : Path parameters
@app.get("/person/deatil/{person_id}", status_code=status.HTTP_200_OK)
def  show_person(
	person_id: int = Path(...,
	gt=0,
	title='Person id'
	,description='this is the  uniqui person id ',example="1")
):
	return{person_id:'it exists¡'}
#validaciones : request body
@app.put("/person/{person_id}", status_code=status.HTTP_202_ACCEPTED)
def update_person(
	person_id: int =Path(
		...,title="Person id",description="this is the person id",gt=0,example="1"
		),person: Person1=Body(...),
Location: Location=Body(...)):
	output= person.dict()
	output.update(Location.dict())

	return output
@app.put('/person/account/', status_code=status.HTTP_200_OK)
def sing_in(person: Person1=Body(...)):
	return person
#forms in fastapi
@app.post(
    path="/login",
    response_model=LoginOut,
    status_code=status.HTTP_200_OK
) 
def login(usename:str =Form(...),password:str =Form(...),):
	return LoginOut(usename=usename)
#cookies and headers
@app.post(
	path="/contact",status_code=status.HTTP_200_OK)
def contact(
	first_name:str =Form(...,min_length=1,max_length=50),
	last_name:str =Form(...,min_length=1,max_length=50),
	email:EmailStr=Form(...),
	message:str =Form(...,min_length=20,max_length=50),
	user_agent: Optional[str]=Header(default=None),
	ads:Optional[str]=Cookie(default=None)

):
	return user_agent
	
