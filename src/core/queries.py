class Queries:
    __query = {
        "<login>": "SELECT getAccountID(%s, %s);",
        "<signup>": "INSERT INTO accounts (username, passcode, privID) VALUES (%s, %s, %s);",
        "<display_cat>": "SELECT catalogID, title, author, stocks FROM catalogs;",
        "<cat_exists>": "SELECT EXISTS(SELECT catalogID FROM catalogs WHERE catalogID = %s);",
        "<borrow_cat>": "INSERT INTO transacts (accountID, catalogID) VALUES (%s, %s);",
        "<recent_tid>": "SELECT transactID FROM transacts WHERE accountID = %s AND catalogID = %s ORDER by borrowDate DESC LIMIT 1",
        "<return_cat>": "DELETE FROM transacts WHERE accountID = %s AND transactID = %s",

        "<get_catalog>": "SELECT * FROM catalogDetails c WHERE c.catalogID = %s",
        "<get_account>": "SELECT * FROM accountDetails a WHERE a.accountID = %s",
        "<get_transact>": "SELECT * FROM transactDetails t WHERE t.`Username` = (SELECT username FROM accounts WHERE accountID = %s) ORDER BY t.`Return Date`;"
    }

    def get(key):
        return Queries.__query[key]

