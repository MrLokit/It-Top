text = """Ежевику для ежат
Принесли два ежа.
Ежевику еле-еле
Ежата возле ели съели."""

wordsStartE = []
words = text.split()

for word in words:
    if word.startswith("е") or word.startswith("Е"):
        wordsStartE.append(word)

count = len(wordsStartE)
print(f'Количество слов: {count}')