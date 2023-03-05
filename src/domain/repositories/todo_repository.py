from abc import ABC, abstractmethod

from src.domain.entitties.todo import Todo


class TodoRepository(ABC):
    @abstractmethod
    async def add(self, todo: Todo) -> Todo:
        pass

    @abstractmethod
    async def get_by_id(self, id) -> Todo | None:
        pass

    @abstractmethod
    async def update(self, id: str, todo: Todo) -> Todo:
        pass

    @abstractmethod
    async def delete(self, id: str) -> None:
        pass

    @abstractmethod
    async def get_all(self) -> list[Todo]:
        pass
