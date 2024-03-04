welcome_massage = ''' 

Первая модернизированная арабица для башкир и татар, подававшая огромные надежды. Элегантная и по - настоящему народная.

Новая тюркская арабица 1920-1927.

 '''
main_menu = ''' 

Напишите слово или предложение  на башкирской или  татарской кириллице, а  бот переведет его на Яна имле.

Башкорт яки татар кириллицасында сүз җөмлә языгыз, бот аны Яңа Имлəге тәрҗемә итәчәк.

Başqort yaki Tatar kirillitsasında süz  cömlə yazığız, bot anı Yaña İmləge tərcemə itəçək.


 '''

extensional_vowels = ["و", "ۇ", "ە", "ىُ", "ي"]

print(welcome_massage)


print(main_menu)



kirill_input = input('Напишите на татарском или на башкирском:')

def kirill_to_arabic(text):
    transliteration_dict = {
        'а': 'ا',
        'б': 'ب',
        'к': 'ك',
        'д': 'د',
        'и': 'ي',
        'ф': 'ف',
        'җ': 'ج',
        'ж': 'ژ',
        'һ': 'ه',
        'ә': 'ە',
        'л': 'ل',
        'м': 'م',
        'н': 'ن',
        'ң': 'ڭ',
        'о': 'ۇ',
        'ө': 'ۇ',
        'п': 'پ',
        'р': 'ر',
        'с': 'س',
        'т': 'ت',
        'ю': 'يو',
        'в': 'ۋ',
        'у': 'و',
        'ү': 'و',
        'й': 'ي',
        'з': 'ز',
        'э': 'ئ',
        'я': 'يا',
        'ш': 'ش',
        'ы': 'ىُ',
        'е': 'ىُ',
        'х': 'خ',
        'г': 'گ',
        'ҡ': 'ق',
        'ғ': 'غ',
        'ҫ': 'ث',
        'ҙ': 'ذ',
        'ч': 'چ',

    }
    result = ""
    for letter in text.lower():
        if letter in transliteration_dict:
            result += transliteration_dict[letter]
        else:
            result += letter
    return result


def add_character(word):
    if len(word) > 1 and word[0] == " ":
        if word[1] in extensional_vowels:
            return "ئ" + word[1:]
    return word



def second_step(sentence):
    result_kirill_to_arabic = kirill_to_arabic(sentence)
    result_add_character = add_character(result_kirill_to_arabic)
    return result_add_character



second_step_result = second_step(kirill_input)




print("У вас получилось ",second_step_result)

    #return kirill_to_arabic + add_character

#def second_step(kirill_input):
    #return add_character(kirill_to_arabic(kirill_input))


#def объединенная_функция(входная_строка):
    #результат_функции_1 = функция_1(входная_строка)
    #результат_функции_2 = функция_2(результат_функции_1)
   # return результат_функции_2

# Вызов объединенной функции
#результат = объединенная_функция("привет")
#print(результат)  # Выведет "ПРИВЕТ!!!"