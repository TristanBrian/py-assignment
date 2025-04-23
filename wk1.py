from main import Pet

def main():
    # Create a pet instance
    my_pet = Pet("Max")

    # Test the pet's methods
    my_pet.eat()
    my_pet.play()
    my_pet.sleep()
    my_pet.train("roll over")
    my_pet.train("play dead")
    my_pet.get_status()

if __name__ == "__main__":
    main()
