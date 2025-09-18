import os, json
import firebase_admin
from firebase_admin import credentials, firestore
from flask import Flask, request, jsonify

app = Flask(__name__)

# Inicializar Firebase
if not firebase_admin._apps:
    if "FIREBASE_CREDENTIALS" in os.environ:
        cred_dict = json.loads(os.environ["FIREBASE_CREDENTIALS"])
        cred = credentials.Certificate(cred_dict)
    else:
        cred = credentials.Certificate("firebase_key.json")  # solo local
    firebase_admin.initialize_app(cred)

db = firestore.client()

@app.route("/")
def home():
    return jsonify({"message": "Bienvenido al Gestor de Tareas con Flask + Firebase!"})

# CRUD de tareas
@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks_ref = db.collection("tasks").stream()
    tasks = [{"id": t.id, **t.to_dict()} for t in tasks_ref]
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    new_task = {"title": data["title"], "done": False}
    doc_ref = db.collection("tasks").add(new_task)
    return jsonify({"id": doc_ref[1].id, **new_task})

@app.route("/tasks/<task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()
    task_ref = db.collection("tasks").document(task_id)
    task_ref.update(data)
    return jsonify({"id": task_id, **data})

@app.route("/tasks/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    db.collection("tasks").document(task_id).delete()
    return jsonify({"message": f"Tarea {task_id} eliminada"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)

