
red = 0
print("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(red, 2, 3, "hello world"))

red = 153
green = 51
blue = 255
print(f"\033[38;2;{red};{green};{blue}mRGB ({red},{green},{blue})")