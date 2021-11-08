from models import Session
def create_entry(model, **kwargs):
    return model(**kwargs)


# def get_entry_by_uid(model_class, id):
#     return model_class.query.get(id)

def get_entry_by_username(model,username):
    return model.query.filter_by(username=username).first()


def delete_entry_by_name(model, username):
    md = model.query.filter_by(username=username).first()
    ss = Session()
    ss.delete(md)

