from schema import db


class DataSet(db.DynamicDocument):
    name = db.StringField(required=True, unique_with=['author'])
    author = db.StringField(required=True)
