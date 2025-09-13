def translate(text):
    VOWELS = {'a', 'e', 'i', 'o', 'u'}
    VOWELS_Y = {'a', 'e', 'i', 'o', 'u', 'y'}
    SPECIALS = {'xr', 'yt'}
    translated = []
    
    for word in text.split():
        if word[0] in VOWELS or word[0:2] in SPECIALS:
            translated.append(word + 'ay')
            continue
            
        for pos in range(1, len(word)):
            if word[pos] in VOWELS_Y:
                if word[pos] == 'u' and word[pos - 1] == 'q':
                    pos += 1
                translated.append(word[pos:] + word[:pos] + 'ay')
                break

    return ' '.join(translated)
