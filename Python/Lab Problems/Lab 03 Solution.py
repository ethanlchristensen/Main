import math

num_words = int(input('Please enter the number of words in the sample: '))
num_sentences = int(input('Please enter the number of sentences in the sample: '))
syllables = int(input('Please enter the number of syllables in the sample: '))
big_words = int(input('Please enter the number of big words in the sample: '))
num_chars = int(input('Please enter the number of characters in the sample: '))

GFI = 0.4 * ((num_words / num_sentences) + (100 * (big_words / num_words)))
print('Gunning Fog Index: {:.4f}'.format(GFI))

kincaid = 206.835 - (1.015 * (num_words / num_sentences)) - (84.6 * (syllables / num_words))
print('Reading Ease Score: {:.4f}'.format(kincaid))

ARI = (4.71 * (num_chars / num_words)) + (0.5 * (num_words / num_sentences)) - 21.43
print('Automated Readbility Index: {:.4f}'.format(ARI))

SMOG = round((math.sqrt(big_words) % 100) / 10) + 3
print('SMOG Index Grade Level: {:d}'.format(SMOG))



# know % 100 gives 10s number i.e 243 % 100 = 43
# 10s number / 10 and round it = closest complete 10s number 43 -> 4.3 -> 4.0
# now we have the closest 10s digit
# tens digit + 3 = SMOG

