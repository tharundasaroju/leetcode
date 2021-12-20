def fullJustify(words: list[str], maxWidth: int) -> list[str]:
    final_words_list = []
    while(len(words) > 0):
        selected_words = select(words, maxWidth)
        final_words_list.append(
            format(selected_words, maxWidth, not len(words) > 0))
    print(final_words_list)
    return final_words_list


def format(words: list[str], maxWidth: int, lastline: bool) -> str:
    formatted_sentence = words.pop(0)
    current_length = len(formatted_sentence)
    if(len(words) == 0):
        formatted_sentence += " "*(maxWidth - current_length)
        return formatted_sentence
    total_word_length = 0
    for word in words:
        total_word_length += len(word)
    space_length = maxWidth - current_length - total_word_length

    if(lastline):
        for word in words:
            formatted_sentence += (" "+word)
            space_length -= 1
        formatted_sentence += " "*space_length
        return formatted_sentence

    wordSpace = int(space_length / len(words))
    remLength = space_length % len(words)

    for word in words:
        numOfSpaces = wordSpace+1 if remLength > 0 else wordSpace
        remLength -= 1
        formatted_sentence += (" "*numOfSpaces + word)
    return formatted_sentence


def select(words: list[str], maxWidth: int) -> list[str]:
    selected_words = [words.pop(0)]
    current_length = len(selected_words[0])
    while(current_length < maxWidth and len(words) > 0):
        word = words.pop(0)
        temp_length = current_length + (len(word)+1)
        if(temp_length <= maxWidth):
            selected_words.append(word)
            current_length = temp_length
        else:
            words.insert(0, word)
            break
    return selected_words


fullJustify(["What","must","be","acknowledgment","shall","be"], 16)
