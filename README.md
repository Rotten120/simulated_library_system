# Library Management System

A modular, database-driven library management system built with Python and MySQL. The system enables users to create accounts, browse and borrow catalogs, manage user privileges, and handle returns and fines, all with robust exception handling and a clear repository structure.

---

## Features

- **Account Management:** Create, log in, and manage user accounts.
- **Catalog Browsing:** View lists of available items, including detailed catalog views.
- **Borrow & Return:** Borrow items and manage returns, including late fines based on user privilege.
- **User Privileges:** Different borrowing limits and fine structures for various user roles.
- **Exception Handling:** Centralized, user-defined exceptions with error codes for maintainability.
- **Unit Testing:** Includes tests for critical functionality like login.
- **Modular Design:** Core logic separated into pages, with a clean repo and script structure.

---

## Getting Started

### Prerequisites

- Python 3.x
- MySQL (localhost instance)
- Required Python packages (read below)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd <repo-directory>
   ```

2. **Install dependencies**
   ```bash
   pip install -r dep/dependencies.txt
   ```
   
3. **Set up the database**
   - Import the scripts from `db_layout/` into your local MySQL instance.
   - Update database credentials as needed.

4. **Run the application**
   ```bash
   python src/main.py
   ```
---

## Usage Overview

- Log in or create a new account.
- Browse the catalog via the `catalog_menu`.
- Select items to view details, borrow, or return.
- Manage your account settings.
- Admin users can manage privileges and system settings.

---

## Contributing

1. Fork the repository and create your branch.
2. Make your changes with clear commit messages.
3. Submit a pull request for review.

---

## Acknowledgements

Thanks to all contributors and users who provided feedback and reported bugs!