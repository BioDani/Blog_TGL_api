from schemas.country_schema import Country
from fastapi import FastAPI, APIRouter, Body, Depends, HTTPException, Path, Query, status, Request
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.database import Session, engine, Base

from models.country_model import Countrie as CountrieModel
from typing import List

from middlewares.jwt_bearer import JWTBearer

country_router = APIRouter()