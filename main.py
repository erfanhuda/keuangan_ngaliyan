from auth import DB_ENGINE as engine, DB_SESSION as session
from model.base import Model
from model.model import * 
import sqlalchemy as sa

if __name__ == '__main__':
    Model.metadata.create_all(engine)
    # Model.metadata.drop_all(engine)
    # all_user = User.query.first()
    # print(all_user)