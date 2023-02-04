# const express = require("express")
from fastapi import FastAPI
import uvicorn
# const HomeRouter = require(...)
from controllers import routes


# create the app object
# const app = express()
app = FastAPI()

# app.use(HomeRouter)
app.include_router(routes)

# app.listen(4000, () = > ...)
uvicorn.run(app, port=4000)