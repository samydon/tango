from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

import os
import api



app = FastAPI(
         title='Tangonet Project',
            description='This is sample code for NGINX Plus  by samjin kim',
            openapi_url='/tango/app/openapi.json'
)

#app.add_middleware(
#    CORSMiddleware,
#    allow_origins={"https://.net", "http://localhost"},
#    allow_credentials=True,
#    allow_methods={"OPTIONS", "GET", "POST"},
#    allow_headers={"*"},
#)
#app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.on_event("startup")
async def startup_event():
   from com.database import engine, Base

  #  Base.metadata.create_all(bind=engine)

#print(os.path.dirname(__file__)) 


@app.get("/")
async def healthcheck():
 
  return {"ok": True}


app.include_router(api.router)
