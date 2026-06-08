import re


def count_specific_word(text, word):
    words = re.findall(r"\b\w+\b", text.lower())
    return words.count(word.lower())


def identify_most_common_word(text):
    words = re.findall(r"\b\w+\b", text.lower())
    if not words:
        return None

    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return max(counts, key=counts.get)


def calculate_average_word_length(text):
    words = re.findall(r"\b\w+\b", text)
    if not words:
        return 0

    return sum(len(word) for word in words) / len(words)


def count_paragraphs(text):
    paragraphs = re.split(r"\n\s*\n", text.strip())
    return len(paragraphs)


def count_sentences(text):
    terminators = re.findall(r"[.!?]+", text)
    return len(terminators) if terminators else 1


if __name__ == "__main__":
    sample_text = (
        "The quick brown fox jumps over the lazy dog. The dog barks!\n\n"
        "Does the fox run? Yes, the fox runs quickly, and the dog watches."
    )
    search_word = "fox"

    print("Specific word count:", count_specific_word(sample_text, search_word))
    print("Most common word:", identify_most_common_word(sample_text))
    print("Average word length:", calculate_average_word_length(sample_text))
    print("Paragraph count:", count_paragraphs(sample_text))
    print("Sentence count:", count_sentences(sample_text))
