def reverse_sentence(sentence):
    return ' '.join(sentence.split()[::-1])

if __name__ == "__main__":
    s = input("Enter a sentence: ")
    print(reverse_sentence(s))