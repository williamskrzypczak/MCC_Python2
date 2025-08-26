class AddressBook:
    """
    Class to represent an address book entry.
    
    This class provides a comprehensive way to store and manage contact information
    for individuals, including personal details and address information.
    
    Attributes:
        first_name (str): The person's first name
        last_name (str): The person's last name
        birthday (str): The person's birthday in MM/DD/YYYY format
        email (str): The person's email address
        street_address (str): The person's street address
        city (str): The person's city
        state (str): The person's state
        zip (str): The person's zip code
        phone (str): The person's phone number
    
    Methods:
        get_first_name(): Returns the first name
        set_first_name(name): Sets the first name
        get_last_name(): Returns the last name
        set_last_name(name): Sets the last name
        get_birthday(): Returns the birthday
        set_birthday(date): Sets the birthday
        get_email(): Returns the email address
        set_email(email): Sets the email address
        get_street_address(): Returns the street address
        set_street_address(address): Sets the street address
        get_city(): Returns the city
        set_city(city): Sets the city
        get_state(): Returns the state
        set_state(state): Sets the state
        get_zip(): Returns the zip code
        set_zip(zip_code): Sets the zip code
        get_phone(): Returns the phone number
        set_phone(phone): Sets the phone number
        display_info(): Prints all contact information in a formatted way
    """
    
    def __init__(self, first_name, last_name, birthday, email, street_address, city, state, zip_code, phone):
        """
        Initialize an AddressBook object with contact information.
        
        Args:
            first_name (str): The person's first name
            last_name (str): The person's last name
            birthday (str): The person's birthday in MM/DD/YYYY format
            email (str): The person's email address
            street_address (str): The person's street address
            city (str): The person's city
            state (str): The person's state
            zip_code (str): The person's zip code
            phone (str): The person's phone number
        """
        self._first_name = first_name
        self._last_name = last_name
        self._birthday = birthday
        self._email = email
        self._street_address = street_address
        self._city = city
        self._state = state
        self._zip = zip_code
        self._phone = phone
    
    # Getter and Setter methods for first_name
    def get_first_name(self):
        """Returns the first name."""
        return self._first_name
    
    def set_first_name(self, name):
        """Sets the first name."""
        self._first_name = name
    
    # Getter and Setter methods for last_name
    def get_last_name(self):
        """Returns the last name."""
        return self._last_name
    
    def set_last_name(self, name):
        """Sets the last name."""
        self._last_name = name
    
    # Getter and Setter methods for birthday
    def get_birthday(self):
        """Returns the birthday."""
        return self._birthday
    
    def set_birthday(self, date):
        """Sets the birthday."""
        self._birthday = date
    
    # Getter and Setter methods for email
    def get_email(self):
        """Returns the email address."""
        return self._email
    
    def set_email(self, email):
        """Sets the email address."""
        self._email = email
    
    # Getter and Setter methods for street_address
    def get_street_address(self):
        """Returns the street address."""
        return self._street_address
    
    def set_street_address(self, address):
        """Sets the street address."""
        self._street_address = address
    
    # Getter and Setter methods for city
    def get_city(self):
        """Returns the city."""
        return self._city
    
    def set_city(self, city):
        """Sets the city."""
        self._city = city
    
    # Getter and Setter methods for state
    def get_state(self):
        """Returns the state."""
        return self._state
    
    def set_state(self, state):
        """Sets the state."""
        self._state = state
    
    # Getter and Setter methods for zip
    def get_zip(self):
        """Returns the zip code."""
        return self._zip
    
    def set_zip(self, zip_code):
        """Sets the zip code."""
        self._zip = zip_code
    
    # Getter and Setter methods for phone
    def get_phone(self):
        """Returns the phone number."""
        return self._phone
    
    def set_phone(self, phone):
        """Sets the phone number."""
        self._phone = phone
    
    def display_info(self):
        """
        Prints all contact information in a nicely formatted way.
        
        This method displays all the contact information for the person
        in a readable format with clear labels.
        """
        print(f"First Name: {self._first_name}")
        print(f"Last Name: {self._last_name}")
        print(f"Birthday: {self._birthday}")
        print(f"Email: {self._email}")
        print(f"Street Address: {self._street_address}")
        print(f"City: {self._city}")
        print(f"State: {self._state}")
        print(f"Zip: {self._zip}")
        print(f"Phone: {self._phone}")
        print()  # Empty line for separation
    
    # Magic Methods
    
    def __str__(self):
        """
        Returns a string representation of the AddressBook object.
        
        Returns:
            str: A formatted string with the person's name and basic info
        """
        return f"{self._first_name} {self._last_name} - {self._email} - {self._phone}"
    
    def __repr__(self):
        """
        Returns an official string representation of the AddressBook object.
        
        Returns:
            str: A detailed string representation suitable for debugging
        """
        return f"AddressBook(first_name='{self._first_name}', last_name='{self._last_name}', birthday='{self._birthday}', email='{self._email}', street_address='{self._street_address}', city='{self._city}', state='{self._state}', zip='{self._zip}', phone='{self._phone}')"
    
    def __eq__(self, other):
        """
        Compares two AddressBook objects for equality.
        
        Two AddressBook objects are considered equal if all their attributes
        have the same values.
        
        Args:
            other: Another AddressBook object to compare with
            
        Returns:
            bool: True if all attributes are equal, False otherwise
        """
        if not isinstance(other, AddressBook):
            return False
        return (self._first_name == other._first_name and
                self._last_name == other._last_name and
                self._birthday == other._birthday and
                self._email == other._email and
                self._street_address == other._street_address and
                self._city == other._city and
                self._state == other._state and
                self._zip == other._zip and
                self._phone == other._phone)


def main():
    """
    Main function to demonstrate the AddressBook class functionality.
    
    Creates four sample AddressBook instances and displays their information
    to demonstrate the class features.
    """
    # Create four instances of AddressBook
    person1 = AddressBook("John", "Doe", "01/01/1990", "john.doe@example.com", 
                         "123 Main St", "Anytown", "NY", "12345", "555-555-5555")
    
    person2 = AddressBook("Jane", "Smith", "02/02/1985", "jane.smith@example.com", 
                         "456 Elm St", "Othertown", "CA", "67890", "555-555-1234")
    
    person3 = AddressBook("Emily", "Johnson", "03/03/1975", "emily.johnson@example.com", 
                         "789 Oak St", "Sometown", "TX", "11111", "555-555-6789")
    
    person4 = AddressBook("Michael", "Brown", "04/04/1965", "michael.brown@example.com", 
                         "101 Pine St", "Anycity", "FL", "22222", "555-555-2468")
    
    # Display information for each person
    print("Address Book Entries:")
    print("=" * 50)
    
    person1.display_info()
    person2.display_info()
    person3.display_info()
    person4.display_info()
    
    # Demonstrate magic methods
    print("Demonstrating Magic Methods:")
    print("=" * 50)
    
    print("String representation (__str__):")
    print(person1)
    print()
    
    print("Official representation (__repr__):")
    print(repr(person1))
    print()
    
    print("Equality comparison (__eq__):")
    person1_copy = AddressBook("John", "Doe", "01/01/1990", "john.doe@example.com", 
                              "123 Main St", "Anytown", "NY", "12345", "555-555-5555")
    print(f"person1 == person1_copy: {person1 == person1_copy}")
    print(f"person1 == person2: {person1 == person2}")
    print()
    
    # Demonstrate getter and setter methods
    print("Demonstrating Getter and Setter Methods:")
    print("=" * 50)
    
    print(f"Original email: {person1.get_email()}")
    person1.set_email("john.doe.updated@example.com")
    print(f"Updated email: {person1.get_email()}")
    print()
    
    print(f"Original phone: {person1.get_phone()}")
    person1.set_phone("555-123-4567")
    print(f"Updated phone: {person1.get_phone()}")


if __name__ == "__main__":
    main()
