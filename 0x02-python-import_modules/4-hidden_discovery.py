#!/usr/bin/python3

if __name__ == "__main__":
    """all names defined by hidden_4 module."""
    import hidden_4

    all_names = dir(hidden_4)
    for name in all_names:
        if name[:2] != "__":
            print(name)
