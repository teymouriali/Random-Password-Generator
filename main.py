import random
import os
from dotenv import load_dotenv
if not os.path.exists(".env"):
    with open(".env", "w") as file:
        file.writelines("""STRING=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
NUMBER=0123456789
PUNCTUATION=!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""")
        file.close()

load_dotenv()

with open(".env", "r") as file:
    strr = os.getenv("STRING")
    number = os.getenv("NUMBER")
    panc = os.getenv("PUNCTUATION")


def main():
    inp = input("Password length ? (enter x for exit) :")
    if inp.lower() == "x":
        exit(0)
    if inp.isnumeric():
        if int(inp) < 1:
            print("must possitive number")
            main()

        if inp.isnumeric() and int(inp) >= 1:
            if inp.lower() == "x":
                exit(0)

            strr2 = strr+number+panc
            pas = "".join(random.choice(strr2) for _ in range(int(inp)))
            print(pas)
            main()

    else:
        main()


if __name__ == "__main__":
    main()
