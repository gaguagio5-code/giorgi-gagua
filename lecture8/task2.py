student = {
    "name": "Giorgi",
    "contacts": {
        "email": "giorgi@example.com",
        "phone": "+995 555 123 456"
    },
    "courses": {
        "python": {"passed": True, "score": 88},
        "web": {"passed": False, "score": 52}
    }
}
print(student["contacts"]["email"])
print(student["courses"]["python"]["score"])
student["courses"]["web"]["passed"] = True
student["courses"]["web"]["score"] = 65
del student["contacts"]["phone"]
print(student)