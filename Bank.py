def main():
    greeting = input("Greeting ")
    reward = "$0"
    name = "Newman"
    if greeting.lstrip().rstrip() == "Hello" or greeting.lstrip().rstrip() == "Hello, " + name or greeting.lstrip().rstrip() == "Hello there" or greeting.lstrip().rstrip() == "Hello ":
        print(reward)
    elif greeting.lstrip().rstrip() == "How you doing?":
        reward = "$20"
        print(reward)
    else:
        reward = "$100"
        print(reward)

main()
