import uuid
from src.common.database import Database
import src.models.users.errors as UserErrors
from src.common.utils import Utils


class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<User {}>".format(self.email)

    @staticmethod
    def is_login_valid(email, password):
          user_data = Database.find_one("users", {"email": email})
          if user_data is None:
              raise UserErrors.UserNotExistsError("User does not exists")
          if not Utils.check_hashed_password(password, user_data["password"]):
              raise UserErrors.IncorrectPasswordError("Password is incorrect")

          return True



