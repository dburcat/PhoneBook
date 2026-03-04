from typing import Dict, List, Optional


class PhoneBook:
    """
    Created by leon on 1/23/18.
    Made WAY better by kristofer 6/16/20
    Python version for beginner coders
    """

    def __init__(self, phonebook_dict: Optional[Dict[str, List[str]]] = None):
        """
        Constructor for PhoneBook
        :param phonebook_dict: Optional dictionary to initialize the phonebook with
        """
        self.phonebook = {} if phonebook_dict is None else phonebook_dict

    def add(self, name: str, phone_number: str) -> None:
        """
        Add a phone number for a contact
        :param name: Contact name
        :param phone_number: Phone number to add
        """
        if name not in self.phonebook:
            self.phonebook[name] = []
        if phone_number not in self.phonebook[name]:
            print(self.phonebook[name])
            self.phonebook[name].append(phone_number)

    def add_all(self, name: str, *phone_numbers: str) -> None:
        """
        Add multiple phone numbers for a contact
        :param name: Contact name
        :param phone_numbers: Variable number of phone numbers to add
        """
        for phone_number in phone_numbers:
            self.add(name, phone_number)

    def remove(self, name: str) -> None:
        """
        Remove a contact from the phonebook
        :param name: Contact name to remove
        """
        if name in self.phonebook:
            del self.phonebook[name]

    def has_entry(self, name: str, phone_number: str = None) -> bool:
        """
        Check if a contact exists, optionally with a specific phone number
        :param name: Contact name to check
        :param phone_number: Optional phone number to check
        :return: True if contact exists (with phone number if specified), False otherwise
        """
        if phone_number is None:
            return name in self.phonebook
        else:
            return name in self.phonebook and phone_number in self.phonebook[name]

    def lookup(self, name: str) -> List[str]:
        """
        Look up all phone numbers for a contact
        :param name: Contact name to look up
        :return: List of phone numbers for the contact
        """
        return self.phonebook.get(name, [])

    def reverse_lookup(self, phone_number: str) -> str:
        """
        Find the contact name for a given phone number
        :param phone_number: Phone number to look up
        :return: Contact name associated with the phone number
        """
        return next((name for name, numbers in self.phonebook.items() if phone_number in numbers), None)

    def get_all_contact_names(self) -> List[str]:
        """
        Get all contact names in the phonebook
        :return: List of all contact names
        """
        return list(self.phonebook.keys())

    def get_map(self) -> Dict[str, List[str]]:
        """
        Get the underlying dictionary representation of the phonebook
        :return: Dictionary mapping names to lists of phone numbers
        """
        return self.phonebook
    
    def __str__(self) -> str:
        """
        String representation of the phonebook
        :return: String representation of the phonebook
        """
        return None
    
def main():
    phone_book = PhoneBook()
    # phone_book.add_all("Joe", "302-555-4444", "302-555-3333", "302-555-2222", "302-555-1111")
    # phone_book.add("John", "302-555-4545")
    # phone_book.add_all("Smith", "302-554-4535", "302-554-4536")
    # phone_book.add("Smith", "302-554-4536")
    # print(phone_book.lookup("Joe"))
    # print(phone_book.has_entry("Joe", "302-555-3333"))
    # print(phone_book.has_entry("Joe", "302-555-9999"))
    # print(phone_book.reverse_lookup("302-555-3333"))
    # print(phone_book.get_all_contact_names())
    # print(phone_book.get_map())
    # print(phone_book.reverse_lookup("302-555-9999"))  # Should return None

if __name__ == "__main__":
    main()