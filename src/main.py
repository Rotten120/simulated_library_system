from core.libsys import LibSys
from pages import *

# remove this <ROOT> and replace all of its instances
# with the informtion necessary before
# executing in your own device
import ROOT

def libsys_init(pages = {}):
    LibSys.init(
        "localhost",
        ROOT.user,      # replace with your superuser
        ROOT.password,  # replace with your superuser's password
        "sim_lib_sys",  # replace with name of database
        pages
    )

def main(starting_page = "main_menu"):
    pages = get_pages()
    libsys_init(pages)
    LibSys.switch_page(starting_page)

if __name__ == "__main__":
    main()
    
