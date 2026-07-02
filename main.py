from wardrobe import load_wardrobe
from recommendation import recommend


def get_occasion():
    """Display menu and return selected occasion."""

    print("\nChoose an occasion:")
    print("1. Class")
    print("2. Work")
    print("3. Casual Outing")
    print("4. Gym")
    print("5. Date Night")
    print("6. Formal Event")
    print("7. Party")
    print("8. Interview")
    print("9. Wedding")
    print("10. Vacation")

    occasions = {
        "1": "class",
        "2": "work",
        "3": "casual outing",
        "4": "gym",
        "5": "date night",
        "6": "formal",
        "7": "party",
        "8": "interview",
        "9": "wedding",
        "10": "vacation"
    }

    while True:
        choice = input("\nEnter your choice (1-10): ")

        if choice in occasions:
            return occasions[choice]

        print("Invalid choice. Please try again.")


def display_outfit(outfit, number):
    """Display a recommended outfit."""

    print(f" Recommendation #{number}")
    print("------------------")

    print(f"Top:      {outfit['outfit'][0]}")
    print(f"Bottom:   {outfit['outfit'][1]}")
    print(f"Shoes:    {outfit['outfit'][2]}")
    print(f"Score:    {outfit['score']:.2f}")


def main():

    print("=" * 45)
    print("      Outfit Recommendation System")
    print("=" * 45)

    wardrobe = load_wardrobe()

    while True:

        try:
            temperature = int(input("\nEnter today's temperature (°F): "))
            break
        except ValueError:
            print("Please enter a valid number.")

    occasion = get_occasion()

    print("\nGenerating recommendations...\n")

    recommendations = recommend(
        wardrobe,
        temperature,
        occasion
    )

    if len(recommendations) == 0:
        print("Sorry! No outfits matched your request.")
        return

    accepted = False

    max_recommendations = min(3, len(recommendations))

    for i in range(max_recommendations):

        display_outfit(recommendations[i], i + 1)

        while True:

            answer = input(
                "\nDo you like this outfit? (yes/no): "
            ).strip().lower()

            if answer in ["yes", "y"]:

                print("\nAwesome, enjoy your outfit!")

                accepted = True
                break

            elif answer in ["no", "n"]:

                if i == max_recommendations - 1:

                    print("\nThose are all the available recommendations.")
                    print("Try changing the weather or occasion.")

                else:

                    print("\nLet's try another outfit...")

                break

            else:

                print("Please type yes or no.")

        if accepted:
            break

    print("\nThank you for using the Outfit Recommendation System!")


if __name__ == "__main__":
    main()