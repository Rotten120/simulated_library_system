class Queries:
    query = {
        "<login>": "SELECT getAccountID(%s, %s);",
        "<signup>": "INSERT INTO accounts (username, passcode, privID) VALUES (%s, %s, %s);",
        "<display_cat>": "SELECT * FROM catalogDetails;",
        "<borrow_cat>": "INSERT INTO transacts (accountID, catalogID) VALUES (%s, %s);",
        "<return_cat>": "DELETE FROM transacts WHERE accountID = %s AND transactID = %s"
    }

    def get(key):
        return Queries.query[key]
