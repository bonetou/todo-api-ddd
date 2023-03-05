from abc import ABC, abstractmethod

from src.domain.entitties.category import Category


class CategoryRepository(ABC):
    @abstractmethod
    def get_all(self) -> list[Category]:
        pass

    @abstractmethod
    def get_by_id(self, id) -> Category | None:
        pass

    @abstractmethod
    def add(self, category: Category) -> Category:
        pass

    @abstractmethod
    def update(self, category: Category) -> Category:
        pass

    @abstractmethod
    def delete(self, id: str) -> None:
        pass
