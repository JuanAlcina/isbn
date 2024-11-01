from repositories.transaction_repository import TransactionRepository

class TransactionService:

    @staticmethod
    def create_transaction_service(data):
        user_id = data['user_id']
        destination = data['destination']
        details = data['details']
        return TransactionRepository.create_transaction_repository(user_id, destination, details)