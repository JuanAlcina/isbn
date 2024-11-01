from repositories.user_repository import UserRepository

class UserService:

    @staticmethod
    def create_user_service(data):
        name = data['name']
        email = data['email']
        phone = data['phone']
        return UserRepository.create_user_repository(name, email)