from consts import CODE_DICTIONARY


def get_decoded(char: str) -> str:
    """
    gets a char and returns the decoded version
    :param char: a char from Ami's code
    :type char: str
    :return: decoded version of the char
    :rtype: str
    """
    if char in CODE_DICTIONARY:
        return CODE_DICTIONARY[char]

    if char.isdigit():
        return " "

    return char


def decode_and_reverse_words(encoded_content):
    # Decode each character
    decoded_chars = [get_decoded(char) for char in encoded_content]

    # Join decoded characters into a string
    joined_string = ''.join(decoded_chars)

    # Split the string into words
    reversed_words = joined_string.split(' ')

    # Reverse each word and join them back together
    decoded_content = ' '.join(word[::-1] for word in reversed_words)

    return decoded_content


def main():
    with open("code.text") as ami_code:
        """
        1) Swap all digits with whitespaces. The rest are being swapped (or not) according to get_decoded()
        content = [' ' if char.isdigit() else get_decoded(char) for char in content]
        2) The result we've got is a list of chars. We want to get a list of words split by " "
        content = ''.join(content).split(' ')
        3) Now, let's reverse the letters of each word in our list, join and print
        content = ' '.join([word[::-1] for word in content])
        """
        #
        encoded_content = ami_code.read()
        decoded_content = ' '.join(
            [word[::-1] for word in ''.join([get_decoded(char) for char in encoded_content]).split(' ')])
        print(decoded_content)

        decoded_content = decode_and_reverse_words(encoded_content)
        print(decoded_content)


if __name__ == "__main__":
    main()
