def create_entry(model, **kwargs):
    return model(**kwargs)


# def get_entry_by_uid(model_class, id):
#     return model_class.query.get(id)

def get_entry_by_username(model,username):
    return model.query.filter_by(username=username).first()