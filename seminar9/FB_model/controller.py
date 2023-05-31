import text
import view
import model

def start():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_pb()
                view.print_message(text.load_successful)
            case 2:
                pass
            case 3:
                pb = model.get_pb()
                view.print_contact(pb, text.load_error)
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass

