from sqlalchemy import Column, Integer, String, LargeBinary, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from .database import Base

class Run(Base):
    __tablename__ = "runs"

    run_id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    client_ip = Column(String, nullable=False)
    filename = Column(String, nullable=False)
    file_size = Column(Integer, nullable=False)
    file_format = Column(String, nullable=False)
    endpoint = Column(String, nullable=False)
    status = Column(Integer, nullable=False)

    inputs = relationship("InputFile", back_populates="run")

class InputFile(Base):
    __tablename__ = "inputs"

    input_id = Column(Integer, primary_key=True, index=True)
    run_id = Column(Integer, ForeignKey("runs.run_id"), nullable=False)
    file_data = Column(LargeBinary, nullable=False)

    run = relationship("Run", back_populates="inputs")
