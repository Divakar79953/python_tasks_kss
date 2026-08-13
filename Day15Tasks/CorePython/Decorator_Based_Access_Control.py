# Decorator-based Access Control

users = {
    "Divakar": "admin",
    "Pooja": "user",
    "Kishore": "guest"
}


def check_role(required_role):

    def decorator(func):

        def wrapper(username):

            if username in users:

                if users[username] == required_role:
                    func(username)
                else:
                    print("Access Denied")

            else:
                print("User not found")

        return wrapper

    return decorator


@check_role("admin")
def admin_dashboard(username):
    print(username, "accessed Admin Dashboard")


@check_role("user")
def user_dashboard(username):
    print(username, "accessed User Dashboard")


admin_dashboard("Divakar")
user_dashboard("Pooja")
admin_dashboard("Pooja")
