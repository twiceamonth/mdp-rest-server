from typing import List

from fastapi import APIRouter

from src.app.views.invitation.crud import get_invitations_for_event
from src.app.views.invitation.crud import create_new_invitation
from src.app.views.invitation.crud import delete
from src.app.db.db_connection import session as db
from src.app.views.invitation.model import InvitationResponse

router = APIRouter(tags=["Приглашения"])

@router.get("/invitations", response_model=list[InvitationResponse])
def get_invitations_list_for_event(event_id: str) -> List[InvitationResponse]:
    return get_invitations_for_event(db, event_id)

@router.post("/invitation", response_model=InvitationResponse)
def create_invitation(invitation: InvitationResponse):
    return create_new_invitation(db, invitation)

@router.delete("/invitations/delete")
def delete_invitation(invitation: InvitationResponse):
    return delete(db, invitation)