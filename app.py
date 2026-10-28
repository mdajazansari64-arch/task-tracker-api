
from flask import Flask, jsonify, request

app = Flask(__name__)

# Temporary in-memory task storage
tasks = []
next_task_id = 1


@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "task-tracker-api"
    }), 200


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify({
        "tasks": tasks,
        "count": len(tasks)
    }), 200


@app.route("/tasks", methods=["POST"])
def create_task():
    global next_task_id

    data = request.get_json(silent=True)

    if not data or not isinstance(data, dict):
        return jsonify({"error": "A JSON object is required"}), 400

    title = data.get("title")

    if not isinstance(title, str) or not title.strip():
        return jsonify({"error": "Task title is required"}), 400

    task = {
        "id": next_task_id,
        "title": title.strip(),
        "completed": False
    }

    tasks.append(task)
    next_task_id += 1

    return jsonify({
        "message": "Task created successfully",
        "task": task
    }), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
