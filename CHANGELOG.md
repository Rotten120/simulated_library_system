# Changelog

---

## v3.2 - "Organizing exception handling"

### Technical Changes
- Created a base class for user-defined exceptions.
- Created an error code class that contains the error number of each error.
- Updated error numbers in MySQL scripts.

### Repository Changes
- User-defined exceptions are now scripted.

### Bug Fixes
- Fixed an issue where `cid_Exists` in `ReturnCat` contained a tuple of lists instead of a boolean.

---

## v3.1 - "Updating borrow catalog page as a catalog menu page"

### Changes
- `Borrow_cat` is now referred to as `catalog_menu`.
- `catalog_menu` now only displays the catalog's ID, title, author, and stocks.
- When a catalog is selected, the user is directed to `cat_details`.
- `cat_details` show full details of the chosen catalog and options for further actions (borrow, etc.).

### Technical Changes
- Query keys are now more informative.
- Logic functions now also return the ID of the data they handled.
- Some procedures have been replaced with queries.

### Repository Changes
- Added unit test for login.
- Procedures that were replaced have been deleted.

---

## v3.0 - "User Privilege and Repository Layout"

### Changes
- Added a maximum borrow count for each user depending on their privilege.
- Added fines for returning late catalogs (cost based on privilege).
- Users can now manage their accounts (change username, password, privilege).

### Technical Changes
- Added `genre` table as array for `catalog.genre` (MySQL does not support arrays).
- Added table for user privileges.
- `LibSys` class now has a commit method.
- Created class to manage user-defined exceptions.
- Created logic method in pages containing core logic and exception handling.

### Repository Changes
- Added a build batch file.
- Source code is now compiled in the `src` folder.
- Each function/procedure in MySQL scripts is now separated.

---

## v2.1 - "Separating functions into scripts"

### Technical Changes
- Each function in `libsys` is separated into its own class, called 'pages'.
- Created `LibSys` class to manage the pages and communicate with the database.
- Added error codes to SQL user-defined exceptions.

### Repository Changes
- The 'pages' classes are now stored inside `core/pages`.
- Scripts in `utils` have been deleted and replaced.

---

## v2.0 - "Integrating MySQL to database"

### Changes
- Log messages now show up to inform users when they have misinputted.

### Technical Changes
- Database management is transferred to MySQL (localhost).
- Queries are now compiled into one file.
- Implemented error handling in some routines.

### Repository Changes
- Added `.gitignore` file.
- Added `db_layout` that stores MySQL scripts.

---

## v1.0 - "First Stable Version"

### Features
- Create accounts.
- Login to accounts.
- Browse and borrow catalogs.
- Return catalogs.
