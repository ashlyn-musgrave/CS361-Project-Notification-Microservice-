# Notifications Microservice

### Overview

This project implements a standalone Notifications microservice using Python and Flask.

This microservice is intended to be called from another program using HTTP requests.  
Below is an example written in Python using the `requests` library.

A separate test client program was written to demonstrate programmatic communication with the microservice using HTTP requests.

---

# Installation

### 1. Create and activate virtual environment for mac

python3 -m venv .venv
source .venv/bin/activate

### 2. Install Dependencies

python3 -m pip install flask requests

---

# Running the Microservice

### 1. Starting the Miroservice

python3 notifications_service.py

  The service runs at: http://127.0.0.1:5002

---

# How to Request Data from the Microservice

### 1. Sending (Requesting) a Notification

        ```python
        import requests
        
        BASE_URL = "http://127.0.0.1:5002"
        
        payload = {
            "user_id": 101,
            "type": "reminder",
            "message": "This notification was sent programmatically."
        }
        
        response = requests.post(f"{BASE_URL}/notify", json=payload)
        
        print("Status Code:", response.status_code)
        print("Response JSON:", response.json())
  
  This code:
  - Sends a POST request to the /notify endpoint
  - Sends JSON data in the request body
  - Programmatically waits for and receives a response from the microservice

---

# How to Receive Data from the Microservice

After sending the request, the client can retrieve data using:

      import requests
      
      BASE_URL = "http://127.0.0.1:5002"
      
      response = requests.get(
          f"{BASE_URL}/notifications",
          params={"user_id": 101}
      )
      
      data = response.json()
      
      print("Status Code:", response.status_code)
      print("Number of Notifications:", data["count"])
      print("Notifications List:", data["notifications"])

  This request:
  - Sends a GET request to retrieve notifications
  - Receives structured JSON from the microservice
  - Programmatically parses the JSON using response.json()
  - Accesses returned values such as count and notifications



# UML Diagram 

![JPEG image-4076-8B1A-B3-0](https://github.com/user-attachments/assets/681f70e7-d1f7-4124-9a2f-3e62c69d4ecc)

