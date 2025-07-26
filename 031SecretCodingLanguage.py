choice = int(input("Enter your choice \n1. Encode \n2. Decode\n"))
msg = input("Enter a message: ")

try:
    match choice:
        case 1:  # Encode
            if len(msg) < 3:
                secret = ''.join(reversed(msg))
            else:
                # Move first letter to the end and add a prefix/suffix
                msg_list = list(msg)
                first_char = msg_list.pop(0)
                msg_list.append(first_char)
                secret = "abc" + ''.join(msg_list) + "cba"
            print(f"The secret code is: {secret}")

        case 2:  # Decode
            if msg.startswith("abc") and msg.endswith("cba"):
                core = msg[3:-3]
                core_list = list(core)
                last_char = core_list.pop()
                core_list.insert(0, last_char)
                decoded = ''.join(core_list)
                print(f"The original message is: {decoded}")
            else:
                # For short messages, assume it's reversed
                decoded = ''.join(reversed(msg))
                print(f"The original message is: {decoded}")

        case _:
            print("Invalid option. Please enter 1 or 2.")

except Exception as e:
    print(f"An error occurred: {e}")
