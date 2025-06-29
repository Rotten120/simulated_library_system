from core.library_system_client import LibSysClient

directory = {
    "account": "database\\account_lists",
    "catalog": "database\\catalog_lists",
    "transact": "database\\transact_lists"
}

def main():
    library = LibSysClient(directory)
    library.start()

if __name__ == "__main__":
    main()
