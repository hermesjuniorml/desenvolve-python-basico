import emoji # type: ignore
print("Emojis disponíveis:")
disponiveis=[":skull:", ":partying_face:", ":honeybee:", ":frog:", ":alien:"]
for i in disponiveis:
    print(f"{emoji.emojize(i)} - {i}")

print("Digite uma frase e ela será emojizada:")
frase=str(input())
print("Frase emojizada:")
print(emoji.emojize(frase))