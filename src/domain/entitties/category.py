class Category:
    def __init__(
        self,
        name: str,
        id: str | None = None,
        description: str | None = None,
    ) -> None:
        self.id = id
        self.name = name
        self.description = description

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Category):
            return False
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)
