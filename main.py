from flask import request, jsonify
from config import app, db
from models import Expense


@app.route("/")
def home():
    return "Hello World"


@app.route("/get", methods=["GET"])
def get_tasks():
    expenses = Expense.query.all()
    json_expenses = list(map(lambda x: x.to_json(), expenses))
    return jsonify({"expenses": json_expenses})


@app.route("/add", methods=["POST"])
def add_expense():
    data = request.get_json()
    price = data['price']
    expense_name = data['expenseName']
    tag = data['tag']
    description = data['description']
    if not price and not expense_name:
        return (
            jsonify(
                {"message": "You must give a price or expense name."}),
            400,
        )
    
    new_expense = Expense(expense_name=expense_name, price=price, tag=tag, description=description)

    try:
        db.session.add(new_expense)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return jsonify({"message": "Expense Added!"}), 201


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
