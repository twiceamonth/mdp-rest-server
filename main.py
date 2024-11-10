from fastapi import FastAPI
import uvicorn
from sqlalchemy.orm import Session
from starlette.staticfiles import StaticFiles

from db.db_connection import engine
from views.event.event_views import router as event_router
from views.biometrics.biometrics_views import router as biometrics_router
from views.department.department_views import router as department_router
from views.employee.employee_views import router as employee_router
from views.invitation.invitation_views import router as invitation_router
from views.position.position_views import router as position_router
from views.visit_mark.visit_mark_views import router as visit_mark_router
from views.visit.visit_views import router as visit_router

app = FastAPI()

app.mount("/biometrics", StaticFiles(directory="biometrics"), name="biometrics")
app.mount("/photos", StaticFiles(directory="photos"), name="photos")
app.mount("/videos", StaticFiles(directory="videos"), name="videos")

app.include_router(event_router)
app.include_router(employee_router)
app.include_router(biometrics_router)
app.include_router(department_router)
app.include_router(invitation_router)
app.include_router(position_router)
app.include_router(visit_mark_router)
app.include_router(visit_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
