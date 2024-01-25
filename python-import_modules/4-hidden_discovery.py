#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    module_words = [name for name in
                    dir(hidden_4) if not name.startswith("__")]
    sorted_words = sorted(module_words)

    for name in sorted_words:
        print(name)
