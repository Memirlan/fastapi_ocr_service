from pydantic import BaseModel

class RunResponse(BaseModel):
    run_id: int
    text: str
