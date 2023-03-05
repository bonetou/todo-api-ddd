from abc import ABC, abstractmethod

from src.domain.entitties.todo import Todo


class TodoRepository(ABC):
    @abstractmethod
    def get_all(self) -> list[Todo]:
        pass

    @abstractmethod
    def get_by_id(self, id) -> Todo | None:
        pass

    @abstractmethod
    def add(self, todo: Todo) -> Todo:
        pass

    @abstractmethod
    def update(self, todo: Todo) -> Todo:
        pass

    @abstractmethod
    def delete(self, id: str) -> None:
        pass
