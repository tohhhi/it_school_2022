from datetime import datetime
import os
import sys

sw_name = "DIGITAL COMPLAINT BOOKLET"
_booklet = []
next_id = 0


def cls():
    os.system("cls" if os.name == "nt" else "clear")


def print_banner(title):
    """Prints program banner."""

    cls()
    print("+", "-" * (len(title) + 2), "+", sep="")
    print("|", title, "|")
    print("+", "-" * (len(title) + 2), "+", sep="")


def print_message(*msg):
    print()
    print("-" * 50)
    print(*msg)
    print("-" * 50)
    print()


def print_complaint(_id, name, text, date):
    print("-" * 20, date, "-" * 20)
    print("ID:", _id)
    print("Reclamant:", name)
    print("Text reclamatie:")
    print(text)
    print("-" * 20, date, "-" * 20)
    print()


def ret_to_main_menu_prompt():
    input("Apasa ENTER pentru a reveni la meniul principal.")


def add_complaint(name, text):
    global next_id
    _booklet.append(
        {
            "id": next_id,
            "name": name,
            "text": text,
            "date": datetime.now(),
            "resolved": False,
        }
    )

    next_id += 1

    # the index of entry in _booklet list will represent complaint id
    return len(_booklet) - 1


def get_complaints_not_done():
    not_done_complaints = []
    for i in _booklet:
        if not i["resolved"]:
            not_done_complaints.append(i)

    return not_done_complaints


def mark_as_done(complaint_id):
    for i in range(len(_booklet)):
        if _booklet[i]["id"] == complaint_id and not _booklet[i]["resolved"]:
            _booklet[i]["resolved"] = True
            return True

    return False


def add_complaint_flow():
    print_banner("Adauga plangere.")

    name = input("Nume: ")
    complaint_text = input("Text plangere: ")

    complaint_id = add_complaint(name, complaint_text)

    print_message("Reclamatie adaugata! Numar:", complaint_id)

    ret_to_main_menu_prompt()


def view_not_done_complaints_flow():
    print_banner("Vezi reclamatiile nerezolvate.")

    complaints = get_complaints_not_done()

    if len(complaints) == 0:
        print_message("Nici o reclamatie noua.")

    for i in complaints:
        print_complaint(i["id"], i["name"], i["text"], i["date"])

    ret_to_main_menu_prompt()


def mark_as_done_flow():
    print_banner("Rezolva reclamatii.")
    _id = input("\nID plangere:")

    if _id.isnumeric() and mark_as_done(int(_id)):
        print_message("Reclamatia cu ID:", _id, "rezolvata.")
    else:
        print_message("Reclamatia cu ID:", _id, "nu a fost gasita.")

    ret_to_main_menu_prompt()


def get_main_menu_choice():
    """Show main menu items asking the user for a choice.
    Returns the function to call next based on user choice.
    """
    choice_ok = False
    m_menu_entries = {
        1: {"text": "Adauga reclamatie.", "f": add_complaint_flow},
        2: {"text": "Vezi reclamatiile.", "f": view_not_done_complaints_flow},
        3: {"text": "Rezolva reclamatii.", "f": mark_as_done_flow},
        0: {"text": "Inchide program.", "f": sys.exit},
    }

    while not choice_ok:
        for k, v in m_menu_entries.items():
            print(k, ". ", v["text"], sep="")
        choice = input("\nAlege un numar: ")
        if not choice.isnumeric() or int(choice) not in m_menu_entries.keys():
            cls()
            print("EROARE: Te rog sa alegi un numar din lista de mai jos.\n\n")
        else:
            choice_ok = True

    return m_menu_entries[int(choice)]["f"]


def main():
    while True:
        print_banner(sw_name)
        current_flow = get_main_menu_choice()
        # call user choice flow
        current_flow()


if __name__ == "__main__":
    main()