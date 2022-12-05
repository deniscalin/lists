
heads_count = 0


while True:
    with open("results.txt", 'r') as file:
        results = file.readlines()

    toss = input("Flip the coin, and enter Heads or Tails here: ")

    match toss:

        case 'Heads':
            results.append(toss + "\n")

            with open("results.txt", "w") as file:
                file.writelines(results)

            for item in results:
                if item.strip("\n") == "Heads":
                    heads_count = heads_count + 1
            heads_percent = (heads_count / len(results)) * 100
            print("Heads: " + str(heads_percent))
            heads_count = 0

        case 'Tails':
            results.append(toss + "\n")

            with open("results.txt", "w") as file:
                file.writelines(results)

            for item in results:
                if item.strip("\n") == "Heads":
                    heads_count = heads_count + 1
            heads_percent = (heads_count / len(results)) * 100
            print("Heads: " + str(heads_percent))
            heads_count = 0

        case _:
            print("This program only accepts Heads or Tails as input! It's really simple, but good like that!")
