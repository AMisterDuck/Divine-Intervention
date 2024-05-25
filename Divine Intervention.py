import random

class Deity:
    def __init__(self):
        self.divine_power = 100

    def bless_crops(self):
        print("You bless the fields with gentle rain.")
        self.divine_power -= 10

    def send_downpour(self):
        print("You send a torrential downpour to quench the thirst of the crops.")
        self.divine_power -= 20

    def teach_irrigation(self):
        print("You teach the farmers advanced irrigation techniques to sustain their crops without rain.")
        self.divine_power -= 15

    def heal_child(self):
        print("You cure the child's illness instantly.")
        self.divine_power -= 30

    def grant_strength(self):
        print("You grant the mother strength and wisdom to cope with whatever comes.")
        self.divine_power -= 10

    def inspire_cure(self):
        print("You inspire the doctors to discover a cure for the child's illness.")
        self.divine_power -= 20

    def enforce_peace(self):
        print("You intervene directly to stop the war and enforce peace.")
        self.divine_power -= 40

    def guide_leaders(self):
        print("You guide the leaders towards reconciliation and negotiation.")
        self.divine_power -= 20

    def inspire_revolution(self):
        print("You inspire the people to rise up against tyranny and fight for their freedom.")
        self.divine_power -= 30

    def display_power(self):
        print(f"Your divine power: {self.divine_power}")

def main():
    deity = Deity()
    while deity.divine_power > 0:
        print("\nPrayer Options:")
        print("1. Bless the fields with rain")
        print("2. Cure the child's illness")
        print("3. Bring peace to the war-torn land")
        print("4. Display Divine Power")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            response = input("How do you wish to bless the fields?\n a) Gentle rain\n b) Torrential downpour\n c) Teach irrigation\nChoice: ")
            if response == 'a':
                deity.bless_crops()
            elif response == 'b':
                deity.send_downpour()
            elif response == 'c':
                deity.teach_irrigation()
            else:
                print("Invalid choice!")
        elif choice == '2':
            response = input("How do you wish to help the child?\n a) Cure illness\n b) Grant strength to mother\n c) Inspire cure\nChoice: ")
            if response == 'a':
                deity.heal_child()
            elif response == 'b':
                deity.grant_strength()
            elif response == 'c':
                deity.inspire_cure()
            else:
                print("Invalid choice!")
        elif choice == '3':
            response = input("How do you wish to bring peace?\n a) Enforce peace\n b) Guide leaders\n c) Inspire revolution\nChoice: ")
            if response == 'a':
                deity.enforce_peace()
            elif response == 'b':
                deity.guide_leaders()
            elif response == 'c':
                deity.inspire_revolution()
            else:
                print("Invalid choice!")
        elif choice == '4':
            deity.display_power()
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
