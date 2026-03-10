# test_client.py

import requests

BASE_URL = "http://127.0.0.1:5002"


def create_notification(user_id: int, message: str, notif_type: str):
    url = f"{BASE_URL}/notify"

    payload = {
        "user_id": user_id,
        "type": notif_type,
        "message": message
    }

    print("\n[TEST CLIENT] Sending POST request to /notify")
    response = requests.post(url, json=payload)

    print("[TEST CLIENT] Status Code:", response.status_code)

    data = response.json()
    print("[TEST CLIENT] Response Data:", data)

    return data


def get_notifications(user_id: int):
    url = f"{BASE_URL}/notifications"

    print("\n[TEST CLIENT] Sending GET request to /notifications")
    response = requests.get(url, params={"user_id": user_id})

    print("[TEST CLIENT] Status Code:", response.status_code)

    data = response.json()
    print("[TEST CLIENT] Response Data:", data)

    return data


def main():
    print("=== TEST PROGRAM START ===")

    user_id = 101

    # Programmatically request data
    create_response = create_notification(
        user_id=user_id,
        message="This notification was created programmatically.",
        notif_type="reminder"
    )

    # Programmatically receive and process returned data
    if create_response.get("ok"):
        notification_id = create_response["notification"]["notification_id"]
        print(f"[TEST CLIENT] Created notification ID: {notification_id}")

    # Programmatically request data again
    list_response = get_notifications(user_id)

    if list_response.get("ok"):
        print(f"[TEST CLIENT] Retrieved {list_response['count']} notifications.")

    print("=== TEST PROGRAM END ===")


if __name__ == "__main__":
    main()