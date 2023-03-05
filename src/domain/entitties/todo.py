from datetime import datetime


class Todo:
    def __init__(
        self,
        title: str,
        description: str,
        category_id: str,
        due_date: datetime,
        id: str | None = None,
        completed: bool = False,
    ) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.category_id = category_id
        self.due_date = due_date
        self.completed = completed

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Todo):
            return False
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)
