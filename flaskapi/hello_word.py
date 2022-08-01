from fastapi import FastAPI
i=788976
app = FastAPI()
@app.get('/')
def home():
	return (1)
