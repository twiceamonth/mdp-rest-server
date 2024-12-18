from typing import List

from fastapi import APIRouter, UploadFile, File, HTTPException, status, Depends

from src.app.views.auth.crud import oauth2_scheme
from src.app.db.db_connection import session as db
from src.app.views.event.crud import *
from src.app.views.event.model import Event, EventResponse, EventPatch

router = APIRouter(tags=["Мероприятия"])


@router.get("/events", response_model=List[EventResponse], dependencies=[Depends(oauth2_scheme)])
def get_events_list() -> List[EventResponse]:
    return get_event_list(db)


@router.get("/events/{event_id}", response_model=EventResponse, dependencies=[Depends(oauth2_scheme)])
def get_event_by_id(event_id: str) -> EventResponse:
    return get_event(db, event_id)


@router.post("/event", response_model=EventResponse, dependencies=[Depends(oauth2_scheme)])
def create_event(event: Event):
    return create_event_post(db, event)


@router.delete("/event/{event_id}", dependencies=[Depends(oauth2_scheme)])
def delete_event(event_id: str):
    return delete(db, event_id)


@router.patch("/event/{event_id}", response_model=EventResponse, dependencies=[Depends(oauth2_scheme)])
def update_event(event_id: str, new_event: EventPatch):
    return update_event_patch(db, event_id, new_event)


@router.post("/upload-event-video/{event_id}", response_model=EventResponse, dependencies=[Depends(oauth2_scheme)])
def upload_event_video(event_id: str, video: UploadFile = File()):
    return upload_video(db, event_id, video)


@router.get("/download-event-video/{event_id}", dependencies=[Depends(oauth2_scheme)])
def download_event_video(event_id: str):
    return download_video(db, event_id)
