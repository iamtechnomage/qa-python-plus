class ContactManager:
    def __init__(self):
        self.contact_list: dict = {}

    def add_contact(self, name: str, phone: int) -> None:
        if self.contact_list.get(name) is not None:
            self.contact_list[name].append(phone)
        else:
            self.contact_list[name] = [phone]

    def add_multiple_contacts(self, contacts: dict[str, list]) -> None:
        for name, phones in contacts.items():
            for phone in phones:
                self.add_contact(name, phone)

    def remove_person_contact_by_id(self, name: str, contact_id: int) -> None:
        if self.contact_list.get(name) is not None:
            try:
                self.contact_list[name].pop(contact_id)
            except IndexError:
                print(f"Contact {name} don't contain phone with id={contact_id}")

    def remove_person_contact_by_phone(self, name: str, phone: int) -> None:
        if self.contact_list.get(name) is not None:
            try:
                self.contact_list[name].remove(phone)
            except ValueError:
                print(f"Contact {name} don't contain phone with number={phone}")

    def remove_person_by_name(self, name: str) -> None:
        try:
            self.contact_list.pop(name)
        except KeyError:
            print(f"Contact with {name} not found")

    def update_contact_phone_number_by_id(self, name: str, contact_id: int, new_phone: int) -> None:
        if self.contact_list.get(name) is not None:
            try:
                self.contact_list[name][contact_id] = new_phone
            except IndexError:
                print(f"Contact {name} don't contain phone with id={contact_id}")

    def show_all_contacts(self) -> None:
        print("----------------------")
        print("Contacts:")
        for name, phones_list in self.contact_list.items():
            print(f"{name}: {phones_list}")
        print("----------------------")

    def show_contact_by_name(self, name: str) -> None:
        try:
            print(f"Found {name} phones: {self.contact_list[name]}")
        except KeyError:
            print(f"Contact with {name} not found")


if __name__ == '__main__':
    app = ContactManager()
    app.add_contact("Man", 88888888888)
    app.add_multiple_contacts({"Den": [78005553535, 78005553536, 78005553537], "Sam": [11111111111, 11111111112]})
    app.show_all_contacts()
    app.remove_person_contact_by_id("Den", 3)
    app.remove_person_contact_by_id("Den", 1)
    app.show_all_contacts()
    app.remove_person_contact_by_phone("Den", 78005553534)
    app.remove_person_contact_by_phone("Den", 78005553535)
    app.show_all_contacts()
    app.remove_person_by_name("Van")
    app.remove_person_by_name("Den")
    app.show_all_contacts()
    app.update_contact_phone_number_by_id("Man", 2, 99999999999)
    app.update_contact_phone_number_by_id("Man", 0, 77777777777)
    app.show_all_contacts()
    app.show_contact_by_name("Den")
    app.show_contact_by_name("Man")
