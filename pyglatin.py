pyg = 'ay'

original = raw_input('Please enter a word: ')

if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
  print 'Translation: ' + new_word
else:
  print 'The word you entered is invalid'