from datetime import datetime, timezone
from models.transaction import Transaction, db

class TransactionRepository:
    @staticmethod
    def create_transaction_repository(user_id, destination, details):
        transaction = Transaction(
            user_id = user_id,
            date = datetime.now(timezone.utc)
            destination = destination,
            status = "Started",
            details = details
        )
        db.session.add(transaction)
        db.session.commit()
        return transaction