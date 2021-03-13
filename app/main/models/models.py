from .. import db
import json, datetime

sales_products = db.Table('sales_products',
    db.Column('product_id', db.Integer, db.ForeignKey('products.product_id')),
    db.Column('quantity', db.Integer),
    db.Column('sale_id', db.Integer, db.ForeignKey('sales.sale_id'))
)

class Products(db.Model):
    
    __tablename__: 'products'

    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    pvp = db.Column(db.Integer)
    cost = db.Column(db.Integer)
    stock = db.Column(db.Integer)
    max_stock = db.Column(db.Integer)
    description = db.Column(db.String)
    provider_id = db.Column(db.Integer, db.ForeignKey('providers.provider_id'))

    def __repr__(self):
        return f"<Product {self.name}>"

    @staticmethod
    def get_by_id(id):
        return Products.query.get(id)

class Providers(db.Model):

    __tablename__ = 'providers'

    provider_id = db.Column(db.Integer, primary_key=True)
    access_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    address = db.Column(db.String)
    company = db.Column(db.String)
    contact_email = db.Column(db.String)
    contact_phone = db.Column(db.String)
    user = db.relationship('Users', back_populates='provider')

    def __repr__(self):
        return f"<Provider id: {self.provider_id}>"

    @staticmethod
    def get_by_id(id):
        return Providers.query.get(id)

class Users(db.Model):

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    access_email = db.Column(db.String)
    password = db.Column(db.String)
    type = db.Column(db.String)
    provider = db.relationship('Providers', uselist=False, back_populates='user')

    def __repr__(self):
        return f"<User {self.name}>"

    @staticmethod
    def get_by_id(id):
        return Users.query.get(id)

    @staticmethod
    def log_in(user):
        return Users.query.filter_by(access_email = user['access_email'], password = user['password']).first()

    @staticmethod
    def register(data):
        new_user = Users(name = data['name'], access_email = data['access_email'], password = data['password'], type = data['type'])
        db.session.add(new_user)
        return db.session.commit()

class Sales(db.Model):

    __tablename__ = 'sales'

    sale_id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)
    date = db.Column(db.DateTime)
    products = db.relationship('Products', secondary=sales_products, lazy="subquery",
        backref=db.backref('sales', lazy=True))

    def __repr__(self):
        return f"<Sale id: {self.sale_id}>"
    
    @staticmethod
    def place(sale_data):
        sale = Sales(amount=sale_data['total'], date=datetime.datetime.utcnow())
        db.session.add(sale)
        db.session.commit()

        for product in sale_data['products']:
            statement = sales_products.insert().values(
                product_id=product['id'],
                quantity=product['quantity'],
                sale_id=sale.sale_id
            )
            db.session.execute(statement)

        db.session.commit()
        return 'Sale placed successfuly'

    @staticmethod
    def get_products(id):
        return Sales.query.get(id).products

class Orders(db.Model):

    __tablename__ = 'orders'

    order_id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)
    date = db.Column(db.DateTime)

    def __repr__(self):
        return f"<Order id: {self.order_id}>"