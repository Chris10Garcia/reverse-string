

# we want to reverse a string
# hello -> olleh
# no built in reserve methods, must use iteration
# the easiest is to pop the end into an another array and append it
# last becomes first
# hello.pop() -> newarray.append(o, l, l, e, h)

# edge case is an empty array... will pop give me issues?

def main(word):

    result = []
    word = list(word)

    while len(word) > 0:
        result.append(word.pop())

    result = "".join(result)
    return result


if __name__ == "__main__":
    test_words = [
        "hello",
        "hi",
        "",
        "catbaby"
    ]
    test_results = [
        "olleh",
        "ih",
        "",
        "ybabtac"
    ]

    for word, result in zip(test_words, test_results):
        answer = main(word)
        assert result == answer, f"The result was {answer}, expected {result}"
        print(f"Successful test for {word}")

