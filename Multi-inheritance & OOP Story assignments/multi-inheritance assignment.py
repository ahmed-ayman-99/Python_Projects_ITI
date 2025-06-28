class Father:
    def __init__(self, last_name):
        self.last_name = last_name
        print(f"Father initialized with last name: {last_name}")


class Mother:
    def __init__(self, eye_color):
        self.eye_color = eye_color
        print(f"Mother initialized with eye color: {eye_color}")


class Uncle (Father):
    def __init__(self ,last_name, hair):
        super().__init__(last_name)
        self.hair = hair
        print (f"Uncle initialized with hair: {hair} and last name: {last_name}")
    

# Inheriting from Father and Mother and Uncle classes
class Child(Mother,Uncle):
    def __init__(self, first_name, last_name, eye_color, hair):
        Uncle.__init__(self, last_name, hair) 
        Mother.__init__(self, eye_color) 
        self.first_name = first_name
        print(f"Child initialized with name: {first_name} {last_name} and eye color: {eye_color} with hair type: {hair}")


Me = Child("Ahmed", "Ayman", "Green", "curly")

