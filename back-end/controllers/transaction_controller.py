from flask import Blueprint, request, jsonify
from services.transaction_service import TransactionService

transaction_api = Blueprint('transaction_api', __name__)

@transaction_api.route('/api/transaction', methods=['POST'])
def create_transaction_controller():
    data = request.get_json()
    TransactionService.create_transaction_service(data)
    return jsonify("Transaction has been successfully created."), 201