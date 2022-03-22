# Author : Nemuel Wainaina

# Program to perform Base64 encoding and decoding on the command line

from colorama import init, Fore
import base64

# initialize the colors
init()
SUCCESS = Fore.GREEN
WARNING = Fore.LIGHTRED_EX
ERROR = Fore.RED
RESULT = Fore.LIGHTYELLOW_EX
RESET = Fore.RESET


# the encoding function
def encode(inp):
    inp = inp.encode()
    try:
        result = base64.b64encode(inp)
    except Exception as e:
        print(f"{ERROR}[-] Oops! Could not encode your input {RESET}")
        print(f"Error Msg => {ERROR}{e} {RESET}")
    else:
        print(f"{SUCCESS}[+] Successfully encoded your input{RESET}")
        print(f"Result :: {RESULT}{result.decode()}{RESET}")


# the decoding function
def decode(inp):
    try:
        result = base64.b64decode(inp)
    except Exception as e:
        print(f"{ERROR}[-] Oops! Could not decode your input {RESET}")
        print(f"Error Msg => {ERROR}{e} {RESET}")
    else:
        print(f"{SUCCESS}[+] Successfully decoded your input {RESET}")
        print(f"Result :: {RESULT}{result.decode()}{RESET}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--enc", dest="enc", help="Msg to encode")
    parser.add_argument("-d", "--dec", dest="dec", help="Msg to decode")
    args = parser.parse_args()

    enc = args.enc
    dec = args.dec

    # we ensure that one of the above arguments was passed, else, print out the appropriate message
    if not enc and not dec:
        # none of them provided
        print(f"{WARNING}[-] You need to provide the input that you want either encoded or decoded {RESET}")
        exit(0)

    elif enc and dec:
        # both arguments supplied
        print(f"{WARNING}[-] Kindly provide one input at a time {RESET}")
        exit(0)

    else:
        # only one of the arguments has been provided
        if enc:
            encode(enc)
        else:
            decode(dec)