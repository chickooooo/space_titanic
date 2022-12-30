def format_as_per_convention(ss: list[str]) -> list[str]:
    lst: list[str] = []
    for s in ss:
        temp: str = ""
        for i, l in enumerate(s):
            if l.isupper():
                if i != 0:
                    temp += "_"
                temp += l.lower()
            else:
                temp += l
        lst.append(temp)
    return lst