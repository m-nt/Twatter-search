import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
import dotenv
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from models.Datatypes import *
from models.Schemas import *
from tools.resolvers import *


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


dotenv.load_dotenv()


@strawberry.type
class Query:
    results: Schema = strawberry.field(resolver=search_twaats)
    echo: Union[str, None] = strawberry.field(resolver=echo)
    pass


schema = strawberry.Schema(Query)

graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
