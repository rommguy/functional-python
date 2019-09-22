def log(message: str, color: str):
    print(message, color)


def test(implemented, code):
    if callable(implemented):
        try:
            code()
        except Exception:
            print("Failed")


def expect(message: str, actual, expected):
    if actual == expected:
        log(
            "OK ...... {message}: {expected} is {actual}".format(
                message=message, expected=expected, actual=actual
            ),
            "green",
        )
    else:
        log(
            "ERROR... {message}: Expected {expected}, but actual is {actual}".format(
                message=message, expected=expected, actual=actual
            ),
            "red",
        )
