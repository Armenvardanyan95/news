alphabet = {
    'ա': 'a',
    'Ա': 'A',
    'բ': 'b',
    'Բ': 'B',
    'գ': 'g',
    'Գ': 'G',
    'դ': 'd',
    'Դ': 'D',
    'ե': 'e',
    'Ե': 'E',
    'զ': 'z',
    'Զ': 'Z',
    'է': 'e',
    'Է': 'E',
    'ը': ['@', 'y'],
    'Ը': ['@', 'Y'],
    'թ': 't',
    'Թ': 'T',
    'ժ': ['g', 'j'],
    'Ժ': ['G', 'J'],
    'ի': 'i',
    'Ի': 'I',
    'լ': 'l',
    'Լ': 'L',
    'խ': ['kh', 'x'],
    'Խ': ['Kh', 'KH', 'x'],
    'ծ': ['c', 'ts'],
    'Ծ': ['c', 'Ts', 'TS'],
    'կ': 'k',
    'Կ': 'K',
    'հ': 'h',
    'Հ': 'H',
    'ձ': 'dz',
    'Ձ': ['Dz', 'DZ'],
    'ղ': ['gh', 'kh', 'x'],
    'Ղ': ['GH', 'Gh', 'Kh', 'KH'],
    'ճ': 'ch',
    'Ճ': ['Ch', 'CH'],
    'մ': 'm',
    'Մ': 'M',
    'յ': ['y', 'i'],
    'Յ': ['Y', 'I'],
    'ն': 'n',
    'Ն': 'N',
    'շ': 'sh',
    'Շ': ['SH', 'Sh'],
    'ո': ['o', 'vo', 'a'],
    'Ո': ['Vo', 'VO'],
    'չ': 'ch',
    'Չ': ['Ch', 'CH'],
    'պ': 'p',
    'Պ': 'P',
    'ջ': ['g', 'j'],
    'Ջ': ['G', 'J'],
    'ռ': 'r',
    'Ռ': 'R',
    'ս': 's',
    'Ս': 'S',
    'վ': 'v',
    'Վ': 'V',
    'տ': 't',
    'Տ': 'T',
    'ր': 'r',
    'Ր': 'R',
    '#': ['u', 'oo'],
    '%': 'U',
    'փ': 'p',
    'Փ': 'p',
    'ք': ['q', 'k'],
    'Ք': ['Q', 'K'],
    'և': 'ev',
    'օ': 'o',
    'Օ': 'O',
    'ֆ': 'f',
    'Ֆ': 'F',
}


def transliterate(armenian_word):
    keywords = ['']
    armenian_word = armenian_word.replace('ու', '#')
    armenian_word = armenian_word.replace('Ու', '#')

    for letter in armenian_word:
        if letter not in alphabet:
            for index, word in enumerate(keywords):
                keywords[index] = word + letter
        elif isinstance(alphabet[letter], list):
            new_keywords = []
            for word in keywords:
                for option in alphabet[letter]:
                    new_keywords.append(word + option)

            keywords = new_keywords[:]
        else:
            for index, word in enumerate(keywords):
                keywords[index] = word + alphabet[letter]

    return '#'.join(keywords)