import json

def main():

    try:
        f = open("Contatos.txt",encoding="utf8")
        jsonObj = json.loads(f.read())
        print(jsonObj)

    except FileNotFoundError:
        print("Arquivo não encontrado!")

if __name__ == '__main__':
    main()
