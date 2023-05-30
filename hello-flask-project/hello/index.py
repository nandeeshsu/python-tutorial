from flask import Flask, jsonify, request

from hello.model.expense import Expense, ExpenseSchema
from hello.model.income import Income, IncomeSchema
from hello.model.transaction_type import TransactionType

app = Flask(__name__)

# incomes = [
#     { 'description': 'salary',
#       'amount': 50000
#     }
# ]

transactions = [
    Income('Salary', 5000),
    Income('Dividends', 200),
    Expense('Pizza', 50),
    Expense('Rock Concert', 100)
]

@app.route("/")
def hello_world():
    return "Welcome to Hello, World Flask project!!!"

@app.route("/api/v1/incomes")
def get_incomes():
    schema = IncomeSchema(many=True)
    incomes = schema.dump(
        filter(lambda t: t.type == TransactionType.INCOME, transactions)
    )
    return jsonify(incomes)

@app.route("/api/v1/incomes", methods=['POST'])
def add_incomes():
    # incomes.append(request.get_json())
    
    return '', 204