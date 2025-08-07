class Queries:
    __query = {
        "<login>": "SELECT getAccountID(%s, %s);",
        "<signup>": "INSERT INTO accounts (username, passcode, privID) VALUES (%s, %s, %s);",
        "<display_cat>": "SELECT catalogID, title, author, stocks FROM catalogs;",
        "<cat_exists>": "SELECT EXISTS(SELECT catalogID FROM catalogs WHERE catalogID = %s);",
        "<borrow_cat>": "INSERT INTO transacts (accountID, catalogID) VALUES (%s, %s);",
        "<recent_tid>": "SELECT transactID FROM transacts WHERE accountID = %s AND catalogID = %s ORDER by borrowDate DESC LIMIT 1",
        "<return_cat>": "DELETE FROM transacts WHERE accountID = %s AND transactID = %s"
    }

    def get(key):
        return Queries.__query[key]

