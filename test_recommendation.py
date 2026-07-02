from wardrobe import load_wardrobe
from recommendation import recommend


def run_test(test_name, temperature, occasion):
    """
    Runs one recommendation test and prints the results.
    """

    wardrobe = load_wardrobe()

    results = recommend(
        wardrobe,
        temperature,
        occasion
    )

   
    print(test_name)
    print("------------------")
    print(f"Temperature: {temperature}°F")
    print(f"Occasion: {occasion}")

    if len(results) == 0:
        print("FAILED - No outfits were recommended.")
        return False

    print(f" PASSED - {len(results)} outfits found.\n")

    top = results[0]

    print("Top Recommendation")
    print("------------------")
    print("Top:    ", top["outfit"][0])
    print("Bottom: ", top["outfit"][1])
    print("Shoes:  ", top["outfit"][2])
    print("Score:  ", round(top["score"], 2))

    return True


def main():

    passed = 0

    tests = [

        ("Test 1 - Warm Weather Class",
         75,
         "class"),

        ("Test 2 - Cold Weather Work",
         45,
         "work"),

        ("Test 3 - Formal Wedding",
         65,
         "wedding"),

        ("Test 4 - Gym",
         82,
         "gym"),

        ("Test 5 - Vacation",
         88,
         "vacation")

    ]

    for test in tests:

        if run_test(*test):
            passed += 1

    print("TEST SUMMARY")
    print(f"Passed: {passed}/{len(tests)}")

    if passed == len(tests):
        print("All tests passed!")
    else:
        print("Some tests failed.")


if __name__ == "__main__":
    main()