#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for lista in dir(hidden_4):
        if (lista[0] != '_' and lista[1] != '_'):
            print(lista)
