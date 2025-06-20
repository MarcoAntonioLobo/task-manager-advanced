from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_task():
    response = client.post("/tasks", json={"title": "Teste", "description": "Descrição de teste"})
    assert response.status_code == 201
    assert "id" in response.json()

def test_list_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_task():
    # Cria uma tarefa para atualizar
    create = client.post("/tasks", json={"title": "Antigo", "description": "desc"}).json()
    task_id = create["id"]

    # Atualiza
    response = client.put(f"/tasks/{task_id}", json={"title": "Novo", "description": "Atualizado"})
    assert response.status_code == 200
    assert response.json()["title"] == "Novo"

def test_delete_task():
    # Cria uma tarefa para deletar
    create = client.post("/tasks", json={"title": "Deletar", "description": "desc"}).json()
    task_id = create["id"]

    # Deleta
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 204
