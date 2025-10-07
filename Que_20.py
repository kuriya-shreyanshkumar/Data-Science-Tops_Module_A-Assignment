class User:
    def __init__(self, user_id, name, password):
        if not password.strip():
            raise ValueError("Password cannot be empty!")

        self.user_id = user_id
        self.name = name
        self.password = self._generate_password(password)

 
    def _generate_password(self, raw_password):
        word = raw_password.split()[0]   
        password = word.capitalize() + "123" + "@#"

        if len(password) <= 8:
            password += "XY"

     
        binary_pass = ' '.join(format(ord(char), '08b') for char in password)
        return binary_pass

    def display_details(self):
        print("\nUser created successfully!\n")
        print("User ID :", self.user_id)
        print("Name    :", self.name)
        print("Binary Password:", self.password)



user_id = input("Enter User ID: ")
name = input("Enter Name: ")
password = input("Enter your password: ")

try:
    user = User(user_id, name, password)   
    user.display_details()
except ValueError as e:
    print("Error:", e)

