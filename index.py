from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from routes.user import router as UserRouter
from routes.auth import router as AuthRouter
from config.database import get_db

db = get_db()
if db:
    print("DB Connected")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail, "statusCode": exc.status_code},
    )


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI"}


app.include_router(AuthRouter)
app.include_router(UserRouter)
