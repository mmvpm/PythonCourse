QA = {
    'Какая версия языка сейчас актуальна?': '"Неверный ответ."',
    'Какая кодировка используется в строках?': 'utf8',
    'Какой оператор сравнения нужно использовать для работы с None и bool?': 'is',
    'Сколько значений есть у bool?': '2'
}

correct_answers = 0
for question, answer in QA.items():
    user_answer = input(question + ' ')
    if user_answer.lower() == answer:
        correct_answers += 1
        print(f'Ответ {user_answer} верен')
    else:
        print('Неверный ответ')

print(f'Правильных ответов: {correct_answers}/{len(QA)}')