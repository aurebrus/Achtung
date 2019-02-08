from passlib.hash import pbkdf2_sha512


@staticmethod
def hash_password(password):
    return pbkdf2_sha512.encrypt(password)

class Utils(object):
    @staticmethod
    def check_hashed_password(password, hashed_password):
        return pbkdf2_sha512.verify(password, hashed_password)
