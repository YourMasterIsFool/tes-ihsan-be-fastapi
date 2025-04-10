from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from delivery.http.task_http import router as task_router
from interface.database.seeder.task_status_seeder import seeder


origins = [
    "http://localhost",
    "http://localhost:5173",
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("⚙️ Starting up... seeding database.")
    await seeder()
    print("✅ Seeder executed.")
    yield
    print("🛑 App shutting down...")


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    error_dict = {}
    for err in exc.errors():
        field = ".".join(str(loc) for loc in err["loc"] if loc != "body")
        error_dict[field] = err["msg"]

    return JSONResponse(status_code=422, content={"errors": error_dict})


app.include_router(task_router)
# app.include_router(task_status_route)
