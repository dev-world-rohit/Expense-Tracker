from config import db


class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    expense_name = db.Column(db.String(200), unique=False, nullable=True)
    price = db.Column(db.String(200), unique=False, nullable=False)
    tag = db.Column(db.String(200), unique=False, nullable=False)
    description = db.Column(db.String(500), unique=False, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "expense_name": self.expense_name,
            "price": float(self.price),
            "tag": self.tag,
            "description": self.description
        }
