# 4.9 Challenge: Turn Your User Into a
# L33t H4x0r
# Write a program called translate.py that asks the user for some input
# with the following prompt:
# Enter some text:
# Use .replace() to convert the text entered by the user into leetspeak
# by making the following changes to lowercase letters:
# • The letter a becomes 4
# • The letter b becomes 8
# • The letter e becomes 3
# 98
# 4.10. Summary and Additional Resources
# • The letter l becomes 1
# • The letter o becomes 0
# • The letter s becomes 5
# • The letter t becomes 7

def translate_1(text):
    for i in text:
        text = text.replace("a", "4")
        text = text.replace("b", "8")
        text = text.replace("e", "3")
        text = text.replace("l", "1")
        text = text.replace("o", "0")
        text = text.replace("s", "5")
        text = text.replace("t", "7")
    return text

trans_table = [('a', '4'), ("b", "8"), ("e", "3"), ("l", "1"),("o", "0"), ("s", "5"), ("t", "7") ]

def translate_2(text):
    for i in range(len(trans_table)):
        text = text.replace(*trans_table[i])
    return text

the_string = input('enter a string: ')

translate1 = translate_1(the_string)
print(f'L33t H4x0R: {translate1}')

translate2 = translate_2(the_string)
print(f'L33t H4x0R: {translate2}')
    





