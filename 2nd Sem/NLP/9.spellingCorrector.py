from textblob import TextBlob


text = open("alicespellingMistake.txt")
textString = ""

for i in text:
    textString += i + " "
    
print('Text with error: ')
print(textString)

textString = TextBlob(textString)
correctedText = textString.correct()

print('\nCorrected Text:')
print(correctedText)