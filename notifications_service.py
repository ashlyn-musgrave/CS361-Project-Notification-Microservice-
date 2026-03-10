# notifications_service.py
from flask import Flask, request, jsonify
import time
import itertools

app = Flask(__name__)

# In-memory notifications storage
NOTIFICATIONS = []  # list of dicts
ID_COUNTER = itertools.count(1)


@app.get("/")
def health():
    return jsonify({
        "ok": True,
        "service": "notifications",
        "endpoints": ["/notify (POST)", "/notifications (GET)"]
    })


@app.post("/notify")
def notify():
    body = request.get_json(silent=True) or {}

    # For a standalone service, the caller provides user_id
    user_id = body.get("user_id")
    message = (body.get("message") or "").strip()
    notif_type = (body.get("type") or "info").strip()

    if user_id is None:
        return jsonify({"ok": False, "error": "user_id is required"}), 400
    if not isinstance(user_id, int):
        # allow numeric strings if you want:
        if isinstance(user_id, str) and user_id.isdigit():
            user_id = int(user_id)
        else:
            return jsonify({"ok": False, "error": "user_id must be an integer"}), 400

    if not message:
        return jsonify({"ok": False, "error": "message is required"}), 400

    notif = {
        "notification_id": next(ID_COUNTER),
        "user_id": user_id,
        "type": notif_type,
        "message": message,
        "created_at_unix": int(time.time()),
        "status": "sent"
    }
    NOTIFICATIONS.append(notif)

    return jsonify({"ok": True, "notification": notif})


@app.get("/notifications")
def list_notifications():
    user_id = request.args.get("user_id", "").strip()
    if not user_id.isdigit():
        return jsonify({"ok": False, "error": "user_id query param required (integer)"}), 400

    uid = int(user_id)
    results = [n for n in NOTIFICATIONS if n["user_id"] == uid]
    return jsonify({"ok": True, "count": len(results), "notifications": results})


if __name__ == "__main__":
    # Runs on http://127.0.0.1:5002
    app.run(host="127.0.0.1", port=5002, debug=True)