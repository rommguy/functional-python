status_file_template = "window.testStatus = {entries}"


def display_result(entries: [str]):
    with open("../presentation/status.js", "w") as status_file:
        status_file.write(status_file_template.format(entries=entries))


class Entry:
    def __init__(self, message, entry_type):
        self.message = message
        self.entry_type = entry_type

    def __repr__(self):
        return '{message: "' + self.message + '", type: "' + self.entry_type + '"}'


class TestApi:
    def __init__(self):
        self.entries = []

    def log(self, message: str, entry_type: str):
        entry = Entry(message, entry_type)
        self.entries.append(entry)
        display_result(self.entries)

    def test(self, implemented, code):
        if callable(implemented):
            try:
                code()
            except Exception as inst:
                self.log(
                    "Error ... Exception thrown: {error}".format(error=inst), "FAIL"
                )

    def expect(self, message: str, actual, expected):
        if actual == expected:
            self.log(
                "OK ...... {message}: {expected} is {actual}".format(
                    message=message, expected=expected, actual=actual
                ),
                "PASS",
            )
        else:
            self.log(
                "ERROR... {message}: Expected {expected}, but actual is {actual}".format(
                    message=message, expected=expected, actual=actual
                ),
                "FAIL",
            )

    def print_entries(self):
        print(self.entries)
