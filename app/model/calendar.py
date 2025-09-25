from dataclasses import dataclass, field
from datetime import datetime, date, time
from typing import ClassVar

from app.services.util import generate_unique_id, date_lower_than_today_error, event_not_found_error, \
    reminder_not_found_error, slot_not_available_error


# TODO: Implement Reminder class here
class Reminder:
@dataclass
EMAIL = "email"
SYSTEM = "system"
def date_time(self,date:date) -> datetime:
    return datetime(date.year, date.month, date.day)
def type(self, string:str=None)->


# TODO: Implement Event class here


# TODO: Implement Day class here


# TODO: Implement Calendar class here
