import typing
from dataclasses import dataclass, field
from datetime import datetime, date, time
from typing import ClassVar

from app.services.util import generate_unique_id, date_lower_than_today_error, event_not_found_error, \
    reminder_not_found_error, slot_not_available_error


#TODO:Implement Reminder class here

@dataclass
class Reminder:

    EMAIL:ClassVar ="email"
    SYSTEM:ClassVar = "system"
    date_time: datetime

    type: str = EMAIL

    def __str__(self):
        return f"Reminder on {self.date_time} of type {self.type}"


#TODO:Implement Event class here

@dataclass
class Event:
    title: str
    description: str
    date_: date
    start_at: time
    end_at: time
    reminders: list[Reminder] = field(default_factory=list)
    id: str = field(default_factory=generate_unique_id)

    def add_reminder(self, date_time: datetime,type: str = Reminder.EMAIL):
        reminder = Reminder(date_time=date_time, type=type)
        self.reminders.append(reminder)

    def delete_reminder(self, reminder_index: int):
        if 0 <= reminder_index < len(self.reminders):
            del self.reminders[reminder_index]
        else:
            reminder_not_found_error()

    def __str__(self):
        return (f"ID: {self.id}\n"
                f"Event title: {self.title}\n"
                f"Description: {self.description}\n"
                f"Time: {self.start_at} - {self.end_at}")
#TODO:Implement Day class here

class Day:
    def __init__(self, date_: date):
        self.date_ = date_
        self.slots: dict[time, str | None] = {}
        self._init_slots()

    def _init_slots(self):
        current_time = time(0, 0)
        while True:
            self.slots[current_time] = None
            total_minutes = current_time.hour * 60 + current_time.minute + 15
            if total_minutes >= 24 * 60:
                break
            hours, minutes = divmod(total_minutes, 60)
            if not (0 <= hours < 24 and 0 <= minutes < 60):
                break
            current_time = time(hours, minutes)


def add_event(self, event_id: str, start_at: time, end_at: time):
        for slot in self.slots:
            if start_at <= slot < end_at:
                if self.slots[slot] is not None:
                    slot_not_available_error()
        for slot in self.slots:
            if start_at <= slot < end_at:
                self.slots[slot] = event_id


def delete_event(self, event_id: str):
    deleted = False
    for slot, saved_id in self.slots.items():
        if saved_id == event_id:
            self.slots[slot] = None
            deleted = True
    if not deleted:
        event_not_found_error()


def update_event(self, event_id: str, start_at: time, end_at: time):
    for slot in self.slots:
        if self.slots[slot] == event_id:
            self.slots[slot] = None

    for slot in self.slots:
        if start_at <= slot < end_at:
            if self.slots[slot]:
                slot_not_available_error()
            else:
                self.slots[slot] = event_id

#TODO:Implement Calendar class here
