import typing
from dataclasses import dataclass, field
from datetime import datetime, date, time
from typing import ClassVar

from app.services.util import generate_unique_id, date_lower_than_today_error, event_not_found_error, \
    reminder_not_found_error, slot_not_available_error


# TODO: Implement Reminder class here

@dataclass
class Reminder:

    EMAIL:ClassVar ="email"
    SYSTEM:ClassVar = "system"
    date_time: datetime

    type: str = EMAIL

    def __str__(self):
        return f"Reminder on {self.date_time} of type {self.type}"


#TODO: Implement Event class here
@dataclass
class Event:
    title: str
    description: str
    date_: date
    start_at: time
    end_at: time

#TODO: Implement Day class here


# TODO: Implement Calendar class here
