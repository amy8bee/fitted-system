from itertools import product


def weather_category(temperature):
    """
    Convert temperature into a weather category.
    """

    if temperature < 55:
        return "cold"
    elif temperature < 75:
        return "mild"
    else:
        return "warm"


def calculate_style_match(style, occasion):
    """
    Returns a score from 0.0 to 1.0 based on
    how well the clothing style matches the occasion.
    """

    occasion_styles = {
        "college class": ["casual"],
        "work": ["work", "casual"],
        "casual outing": ["casual"],
        "gym": ["gym"],
        "date night": ["casual", "formal"],
        "formal": ["formal"],
        "party": ["casual", "formal"],
        "interview": ["work", "formal"],
        "wedding": ["formal"],
        "vacation": ["casual"]
    }

    if style in occasion_styles.get(occasion, []):
        return 1.0

    return 0.3


def calculate_weather_match(item_weather, current_weather):
    """
    Returns 1 if the clothing is appropriate
    for the weather.
    """

    if current_weather in item_weather:
        return 1.0

    return 0.0


def calculate_occasion_match(style, occasion):
    """
    Additional occasion score.
    """

    if occasion == "formal":
        return 1.0 if style == "formal" else 0.2

    if occasion == "gym":
        return 1.0 if style == "gym" else 0.2

    if occasion == "work":
        return 1.0 if style in ["work", "formal"] else 0.6

    if occasion == "interview":
        return 1.0 if style in ["formal", "work"] else 0.4

    if occasion == "wedding":
        return 1.0 if style == "formal" else 0.2

    return 1.0


def calculate_score(style_match,
                    wardrobe_match,
                    weather_match,
                    occasion_match):
    """
    Weighted recommendation score.
    """

    return (
        0.35 * style_match +
        0.30 * wardrobe_match +
        0.20 * weather_match +
        0.15 * occasion_match
    )


def recommend(wardrobe, temperature, occasion):

    weather = weather_category(temperature)

    outfits = []

    tops = wardrobe["tops"]
    bottoms = wardrobe["bottoms"]
    shoes = wardrobe["shoes"]

    for top, bottom, shoe in product(tops, bottoms, shoes):

        # Weather filter

        if weather not in top["weather"]:
            continue

        if weather not in bottom["weather"]:
            continue

        if weather not in shoe["weather"]:
            continue

        # Determine overall style

        styles = [
            top["style"],
            bottom["style"],
            shoe["style"]
        ]

        if "formal" in styles:
            outfit_style = "formal"

        elif "work" in styles:
            outfit_style = "work"

        elif "gym" in styles:
            outfit_style = "gym"

        else:
            outfit_style = "casual"

        style_match = calculate_style_match(
            outfit_style,
            occasion
        )

        wardrobe_match = 1.0

        weather_match = (
            calculate_weather_match(top["weather"], weather) +
            calculate_weather_match(bottom["weather"], weather) +
            calculate_weather_match(shoe["weather"], weather)
        ) / 3

        occasion_match = calculate_occasion_match(
            outfit_style,
            occasion
        )

        score = calculate_score(
            style_match,
            wardrobe_match,
            weather_match,
            occasion_match
        )
        # Save the outfit and its score
        outfits.append(
            {
                "outfit": [
                    top["name"],
                    bottom["name"],
                    shoe["name"]
                ],
                "style": outfit_style,
                "score": score
            }
        )

    # Sort outfits from highest score to lowest score
    outfits.sort(
        key=lambda outfit: outfit["score"],
        reverse=True
    )

    # Remove duplicate outfits (if any)
    unique_outfits = []
    seen = set()

    for outfit in outfits:

        key = tuple(outfit["outfit"])

        if key not in seen:
            unique_outfits.append(outfit)
            seen.add(key)

    return unique_outfits
