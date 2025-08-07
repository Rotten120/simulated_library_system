from .change_username import ChangeUser
from .change_password import ChangePass
from .change_privilege import ChangePriv

def get_pages():
    return {
        "change_user": ChangeUser,
        "change_pass": ChangePass,
        "change_priv": ChangePriv
    }
