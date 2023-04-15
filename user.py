class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)

    def enroll(self):
        if self.is_rewards_member:
            print("User already a member.")
            return False
        self.is_rewards_member = True
        self.gold_card_points = 200

    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print("You don't have enough points.")
            return # exit function!
        self.gold_card_points -= amount

my_user = User("Inbum", "Baek", "inbumbaek@gmail.com", 33)
my_user.display_info()
my_user.enroll()
my_user.display_info()
my_user.spend_points(50)
my_user.display_info()