import enum

class VisitStatus(str, enum.Enum):
    WAITING = "WAITING"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"
    CANCEL = "CANCEL"
    NO_SHOW = "NO_SHOW"