from sqlalchemy import Column, ForeignKey, text, UUID, String, Text

from src.app.db.models.department import DepartmentDTO
from src.app.db.models.position import PositionDTO
from src.app.db.base import Base


class EmployeeDTO(Base):
    __tablename__ = "Employee"
    __table_args__ = {"schema": "mdp"}

    employee_id = Column(
        UUID,
        primary_key=True,
        server_default=text("nextval('employee_id_seq'::regclass)"),
    )
    first_name = Column(String(100))
    second_name = Column(String(100))
    patronymic = Column(String(100), nullable=True)
    employee_photo = Column(Text)
    department_id = Column(ForeignKey(DepartmentDTO.department_id), nullable=False)
    position_id = Column(ForeignKey(PositionDTO.position_id), nullable=False)

    #position = relationship("Position")
    # , primaryjoin="Employee.position_id == Position.position_id"
    #department = relationship("Department")
    # , primaryjoin="Employee.department_id == Department.department_id"
