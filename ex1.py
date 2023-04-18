import csv


def get_connections() -> dict[int, list[tuple[int, int]]]:
    connections = {}
    with open("./graph_example.csv", encoding="utf-8") as f:
        book = csv.reader(f)
        for line in book:
            user_id = int(line[0])
            contact_id = int(line[1])
            contact_weight = int(line[2])
            contact_data = (contact_id, contact_weight)
            if user_id not in connections:
                connections[user_id] = [contact_data]
            else:
                connections[user_id].append(contact_data)

    return connections


def get_targets() -> dict[int, float]:
    targets = {}
    with open("./target.csv", encoding="utf-8") as f:
        book = csv.reader(f)
        for line in book:
            user_id = int(line[0])
            target = float(line[1])
            targets[user_id] = target

    return targets


def main():
    connections = get_connections()
    targets = get_targets()

    print(connections)
    print(targets)


if __name__ == "__main__":
    main()
