with open('1.txt', 'r', encoding='utf-8') as file:
    for i in file:
        print(i)
author = input('Хто написав ці рядки?')
with open('1.txt', "a", encoding='utf-8') as file:
    file.write(author)
while True:
    answer = input('Бажаэте додати ще цитату? (так/ні)')
    if answer == 'так':
        quote = input('Введіть цитату:')
        author = input('Введіть автора:')
        with open('1.txt', 'a', encoding='utf-8') as file:
            file.write(quote + '\n' + author + '\n')
    else:
        break
with open('1.txt', 'r', encoding='utf-8') as file:
    for i in file:
        print(i)
