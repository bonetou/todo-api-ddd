from src.domain.entitties.todo import Todo
from src.domain.repositories.todo_repository import TodoRepository


class TodoService:
    def __init__(self, todo_repository: TodoRepository):
        self.todo_repository = todo_repository

    async def create(self, todo: Todo) -> Todo:
        return await self.todo_repository.add(todo)

    async def update(self, id: str, todo: Todo) -> Todo:
        return await self.todo_repository.update(id, todo)

    async def delete(self, id: str) -> None:
        await self.todo_repository.delete(id)

    async def get_by_id(self, id: str) -> Todo | None:
        return await self.todo_repository.get_by_id(id)

    async def get_all(self) -> list[Todo]:
        return await self.todo_repository.get_all()
