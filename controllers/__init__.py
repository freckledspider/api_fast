# const Router = require("express").Router
from fastapi import APIRouter

# const router = Router()
routes = APIRouter(prefix="")

# router.get("/", (req, res) => ...)
@routes.get("/")
async def home():
    return {"home": "The home route"}