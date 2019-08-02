digits = ['1','2','3','4','5','6','7','8','9']
en = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
fr = ['un','deux','trois','quatre','cinq','six','sept','huit','neuf']


translate_dictionary = {}

for digit in range(len(digits)):
    translate_dictionary[digit+1] = {'French': fr[digit], 'English': en[digit]}


print(translate_dictionary)