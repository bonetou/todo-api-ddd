from datetime import datetime


class Todo:
    def __init__(
        self,
        title: str,
        description: str,
        category_id: str,
        due_date: datetime,
        completed: bool = False,
    ) -> None:
        self._id: str | None = None
        self.title = title
        self.description = description
        self.category_id = category_id
        self.due_date = due_date
        self.completed = completed

    @property
    def id(self) -> str | None:
        return self._id

    def assign_id(self, id: int) -> None:
        if self._id is not None:
            raise ValueError("Todo ID is already set")
        self._id = id

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Todo):
            return False
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)
