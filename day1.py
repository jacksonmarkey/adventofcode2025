def main():
    counter = 50
    pt_1_clicks = 0
    pt_2_clicks = 0
    with open("secret.txt") as file:
        for line in file:
            direction = line[0]
            distance = int(line[1:])
            # print(f"counter:{counter}")
            # print(f"{direction}{distance}")
            if direction == "L":
                new_counter = counter - distance
            else:
                new_counter = counter + distance
            if new_counter % 100 == 0:
                pt_1_clicks += 1
            # print(f"new_counter:{new_counter}")
            # print(f"add:{abs(new_counter // 100 - counter // 100)}")
            pt_2_clicks += abs(new_counter // 100 - counter // 100)
            if counter % 100 == 0 and direction == "L":
                pt_2_clicks -= 1
            if new_counter % 100 == 0 and direction == "L":
                pt_2_clicks += 1
            counter = new_counter
    print(pt_1_clicks)
    print(pt_2_clicks)


if __name__=="__main__":
    main()