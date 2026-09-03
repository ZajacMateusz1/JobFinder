class AuthRepository:
    def create_user(self, username: str, hashed_password: str, email: str) -> dict:
        return {
            "username": username,
            "email": email,
        }
