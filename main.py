from openai import OpenAI

def main():
    strawberry_kcal = 0.33
    daily_kcal = 2250
    strawberries_needed = round(daily_kcal/strawberry_kcal,2)
    print(f"Potrzebujesz {strawberries_needed} truskawek")
    return strawberries_needed

def lepszy_main():
    api_key = input("Podaj klucz OpenAI:\n")
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
            model="gpt-4o-2024-08-06",
            messages=[
                {"role": "system", "content": "Zwracaj jedynie odpowiedź w formie liczby zmiennoprecinkowej"},
                {"role": "user", "content": """
                Zakładamy, że 100 gramów truskawki zawiera 33 kcal, przeciętne dzienne
                zapotrzebowanie kcal dla człowieka, to 2250 kcal, a cała energia pochodzi 
                wyłącznie z truskawek – nie ma innych źródeł kalorii. Zmiennoprzecinkowa 
                liczba truskawek w gramach zaokragląna do dwóch miejsc po przecinku
                """},
            ], 
            temperature=0.0,
            max_tokens=10
        )
    openai_choice = response.choices[0].message.content
    print(f"Potrzebujesz {openai_choice} truskawek")
    return openai_choice

main()