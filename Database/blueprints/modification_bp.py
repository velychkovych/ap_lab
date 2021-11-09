from database.models import modification
from database.dbUtils import *
from database.schemas import ModificationSchema


@app.route("/article/modification", method="POST")
def create_modification():
    return create_entry(ModificationSchema, modification)

# post modification
# get all versions of article
# get all modification of article
# get modification by id
# put article
# delete modification
