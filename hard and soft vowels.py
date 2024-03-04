#Гласные звуки подразделяются на твердые и мягкие.
#Калын сузыклар (твердые гласные) [а] [у] [о] [ы] [о] [ы].
# Нечкә сузыклар (мягкие гласные) [ә] [ү] [ө] [е] [и] [э].
#ق ك
#گ غ
#
#
#




import telebot
BOT_TOKEN = '6568769535:AAFFH7TPvrWlBh-ikdMEdrZd4BbDDXdV6_I'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def handle_message(message):
    bot.reply_to(message, 'Напишите текст на татарском или на башкирском языке')
@bot.message_handler(content_types=['text'])

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

    }
    result = ""
    for letter in text.lower():
        if letter in transliteration_dict:
            result += transliteration_dict[letter]
        else:  # keep original character if it's not in the dictionary
            result += letter
    return result
extensional_vowels = ["و","ۇ","ە","ىُ","ي"]
if extensional_vowels in result:
def add_character(word):
    if len(word) > 1 and word[0] == " ":
        if word[1] in extensional_vowels:
            return "ئ" + word[1:]
    return word
def handle_message(message):
    bot.reply_to(message, message.word)
bot.polling()