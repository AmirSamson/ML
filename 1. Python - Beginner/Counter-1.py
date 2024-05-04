text = """ WEB-APP TESTING, MANUAL TESTING, FUNCTIONAL TESTING, NON-FUNCTIONAL TESTING, REGRESSION TESTING, BLACK BOX TESTING, INTEGRATION TESTING, COMPATIBILITY TESTING, PERFORMANCE TESTING"""

print(text.lower().split())


word_count = {}

for x in text.lower().split():
    if x in word_count:
        word_count[x] += 1 
    else:
        word_count[x] = 1

print(word_count)
