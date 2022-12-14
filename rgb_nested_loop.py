#!/usr/bin/env python3

# Created By: Peter Sobowale
# Date: November 16, 2022
# This program prints every possible RGB color


def main():
    # initialize variables
    red = 0
    green = 0
    blue = 0

    # for loop to print every color possibility
    for red in range(256):
        # print color
        print(f"\033[38;2;{red};{green};{blue}mRGB ({red},{green},{blue})")
        # for loop to print every color possibility
        for green in range(256):
            # print color
            print(f"\033[38;2;{red};{green};{blue}mRGB ({red},{green},{blue})")
            # for loop to print every color possibility
            for blue in range(256):
                # print color
                print(f"\033[38;2;{red};{green};{blue}mRGB ({red},{green},{blue})")

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
