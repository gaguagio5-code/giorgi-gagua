from functools import wraps


def require_role(allowed_role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if kwargs.get("user_role") == allowed_role:
                return func(*args, **kwargs)
            print(f"Permission Denied: User is not an {allowed_role}.")
        return wrapper
    return decorator


@require_role(allowed_role="admin")
def delete_user(username, user_role=None):
    """Deletes a user from the system."""
    return f"User {username} deleted"


print(delete_user("bob", user_role="admin"))   # User bob deleted
print(delete_user("bob", user_role="guest"))   # Permission Denied: User is not an admin.
print(delete_user.__name__)                    # delete_user
print(delete_user.__doc__)                     # Deletes a user from the system.