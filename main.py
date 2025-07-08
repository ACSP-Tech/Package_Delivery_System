#objective:Manage a collection of books that users can borrow and return.
from delivery_utils import check_filepath

check_filepath()



def delivery_system():
    from delivery_utils import menu
    while True:
        options = menu()
        if options == 1:
            from delivery_utils import register_option
            register_option()
            print()
        elif options == 2:
            from delivery_utils import markdelivered_option
            markdelivered_option()
            print()
        elif options == 3:
            from delivery_utils import view_option
            view_option()
            print()
        elif options == 4:
            from delivery_utils import save_to_file
            save_to_file()
        elif options == 5:
            from delivery_utils import load_from_file
            load_from_file()
        else:
            ("bye")
            break

delivery_system()

