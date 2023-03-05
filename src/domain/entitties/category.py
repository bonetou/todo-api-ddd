class Category:
    def __init__(
        self,
        name: str,
        description: str | None = None,
    ) -> None:
        self._id = None
        self.name = name
        self.description = description

    @property
    def id(self) -> str | None:
        return self._id

    def assign_id(self, id: str) -> None:
        if self._id is None:
            self._id = id
        raise ValueError("Id already assigned")

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Category):
            return False
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)
