from openai import OpenAI

def main():
    strawberry_kcal = 0.33
    daily_kcal = 2250
    strawberries_needed = round(daily_kcal/strawberry_kcal,2)
    print(f"Potrzebujesz {strawberries_needed} truskawek")
    return strawberries_needed

main()