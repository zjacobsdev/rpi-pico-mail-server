import uuid
from datetime import datetime
from pydantic import BaseModel, Field
from typing import List,Optional

class DeviceResponseBase(BaseModel):
     id: str =Field(default_factory= uuid.uuid4, alias="_id")
     start_uptime: Optional[datetime]  
     is_mailbox_open: Optional[bool]
     class Config:
          orm_mode = True