'''
För att få åka Balder på Liseberg måste man vara 130 cm lång. Skriv ett program som kan säga om man får åka!
Fråga användaren hur lång man är (i cm)
Skriv ut antingen "Du får åka!" eller "Du får inte åka"
Skriv in följande värden för att testa att ditt program gjort rätt:
121 cm (får inte åka)
130 cm (får åka)
155 cm (får åka)
'''
user_height = int(input("How long are you? Please enter your height in cm: "))

if user_height == 129:
    print("You can not go")
elif user_height == 130:
    print("You can go")
elif user_height == 155:
    print("You can go")
elif user_height !=129 and user_height !=130 and user_height !=155:
    print("Please try again")


