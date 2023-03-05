import pytest
from src.domain.entitties.todo import Todo
from src.domain.repositories.todo_repository import TodoRepository
from src.domain.services.todo_service import TodoService


class TodoRepositoryInMemory(TodoRepository):
    def __init__(self):
        self.todos: list[Todo] = []

    async def add(self, todo: Todo) -> Todo:
        todo.assign_id(str(len(self.todos) + 1))
        self.todos.append(todo)
        return todo

    async def get_by_id(self, id) -> Todo | None:
        filtered = list(filter(lambda todo: todo.id == id, self.todos))
        if len(filtered) > 0:
            return filtered[0]
        return None

    async def update(self, id: str, todo: Todo) -> Todo:
        try:
            todo.assign_id(id)
            self.todos[int(id) - 1] = todo
            return self.todos[int(id) - 1]
        except KeyError:
            raise Exception("Todo not found")

    async def delete(self, id: str) -> None:
        try:
            index = next(i for i, t in enumerate(self.todos) if t.id == id)
            self.todos.pop(index)
        except StopIteration:
            raise Exception("Todo not found")

    async def get_all(self) -> list[Todo]:
        return self.todos


@pytest.mark.asyncio
async def test_todo_service_should_create_todo():
    todo_service = TodoService(todo_repository=TodoRepositoryInMemory())
    new_todo = Todo(
        title="Test",
        description="Test description",
        category_id="1",
        due_date="2021-01-01",
        completed=False,
    )
    created_todo = await todo_service.create(new_todo)
    assert created_todo is not None
    assert created_todo.id == "1"
    assert created_todo.title == "Test"
    assert created_todo.description == "Test description"
    assert created_todo.category_id == "1"
    assert created_todo.due_date == "2021-01-01"
    assert created_todo.completed == False


@pytest.mark.asyncio
async def test_todo_service_should_update_todo():
    todo_service = TodoService(todo_repository=TodoRepositoryInMemory())
    new_todo = Todo(
        title="Test",
        description="Test description",
        category_id="1",
        due_date="2021-01-01",
        completed=False,
    )
    created_todo = await todo_service.create(new_todo)

    updated_todo = await todo_service.update(
        id=created_todo.id,
        todo=Todo(
            title="Test updated",
            description="Test description updated",
            category_id="1",
            due_date="2021-01-01",
            completed=True,
        ),
    )
    assert updated_todo is not None
    assert updated_todo.id == "1"
    assert updated_todo.title == "Test updated"
    assert updated_todo.description == "Test description updated"
    assert updated_todo.category_id == "1"
    assert updated_todo.due_date == "2021-01-01"
    assert updated_todo.completed == True


@pytest.mark.asyncio
async def test_todo_service_should_delete_todo():
    todo_service = TodoService(todo_repository=TodoRepositoryInMemory())
    new_todo = Todo(
        title="Test",
        description="Test description",
        category_id="1",
        due_date="2021-01-01",
        completed=False,
    )
    created_todo = await todo_service.create(new_todo)

    await todo_service.delete(id=created_todo.id)
    assert len(await todo_service.get_all()) == 0


@pytest.mark.asyncio
async def test_todo_service_should_get_todo_by_id():
    todo_service = TodoService(todo_repository=TodoRepositoryInMemory())
    new_todo = Todo(
        title="Test",
        description="Test description",
        category_id="1",
        due_date="2021-01-01",
        completed=False,
    )
    created_todo = await todo_service.create(new_todo)

    todo = await todo_service.get_by_id(id=created_todo.id)
    assert todo is not None
    assert todo.id == "1"
    assert todo.title == "Test"
    assert todo.description == "Test description"
    assert todo.category_id == "1"
    assert todo.due_date == "2021-01-01"
    assert todo.completed == False


@pytest.mark.asyncio
async def test_todo_service_should_get_all_todos():
    todo_service = TodoService(todo_repository=TodoRepositoryInMemory())
    new_todo = Todo(
        title="Test",
        description="Test description",
        category_id="1",
        due_date="2021-01-01",
        completed=False,
    )
    await todo_service.create(new_todo)

    new_todo = Todo(
        title="Test 2",
        description="Test description 2",
        category_id="1",
        due_date="2021-01-01",
        completed=False,
    )
    await todo_service.create(new_todo)

    todos = await todo_service.get_all()
    assert todos is not None
    assert len(todos) == 2

    assert todos[0].id == "1"
    assert todos[0].title == "Test"
    assert todos[0].description == "Test description"
    assert todos[0].category_id == "1"
    assert todos[0].due_date == "2021-01-01"
    assert todos[0].completed == False

    assert todos[1].id == "2"
    assert todos[1].title == "Test 2"
    assert todos[1].description == "Test description 2"
    assert todos[1].category_id == "1"
    assert todos[1].due_date == "2021-01-01"
    assert todos[1].completed == False
