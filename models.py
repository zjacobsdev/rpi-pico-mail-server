from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from configs.db_config import Base


class User(Base):
    __tablename__ = "mailbox_events"

    id = Column(Integer, primary_key=True, index=True)
    device_uptime = Column(String, unique=True, index=True)
    is_mail_open = Column(Boolean, default=False)
