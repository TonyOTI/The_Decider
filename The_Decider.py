import random
import re


def main():

    is_running = True

    while is_running:

        choices = []

        choice1 = (input("What is one of the choices? (You may add multiple choices separated by a comma)\n"))
        if "," in choice1:
            temp_arr = choice1.split(",")
            for item in temp_arr:
                item = re.sub(r"^\s+|\s+$", "", item)
                if item == "":
                    continue
                choices.append(item)
        else:
            choice1 = re.sub(r"^\s+|\s+$", "", choice1)
            if choice1 == "":
                continue
            choices.append(choice1)

        i = 0
        while i < 100:
            print()
            more_choices = input("Any more? (Type 'end' to get your result)\n")
            if i == 99:
                print("Last chance, kid.\n")
            if re.search("^end$", more_choices, re.IGNORECASE):
                break
            if "," in more_choices:
                temp_arr = more_choices.split(",")
                for item in temp_arr:
                    item = re.sub(r"^\s+|\s+$", "", item)
                    if item == "":
                        continue
                    choices.append(item)
            else:
                more_choices = re.sub(r"^\s+|\s+$", "", more_choices)
                if more_choices == "":
                    continue
                choices.append(more_choices)
            i += 1
            
        print("\n")

        print(f"I've decided on this: {random.choice(choices)}\n\n")

        while is_running:
            run_again = input("Deal with it. Go again? (Y/n)\n")
            if run_again.upper() not in ["Y", "N", "", "YES", "NO"]:
                print("Invalid input. Please enter Y or N.")
                continue
            if run_again.upper() in ["N", "NO"]:
                is_running = False
            break
        


if __name__ == "__main__":
    main()