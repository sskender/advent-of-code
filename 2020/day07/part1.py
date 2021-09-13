import re
import sys

raw_rules = sys.stdin.read().strip().split("\n")

bags_map = dict()
for raw_rule in raw_rules:
    parts = raw_rule.split("bags contain")
    master_bag = parts[0].strip()
    slave_bags_raw = [bag.strip() for bag in re.split("bags?[,\\.]", parts[1]) if (bag and "no other" not in bag)]
    slave_bags = list()
    for slave_bag in slave_bags_raw:
        bag = " ".join(slave_bag.split(" ")[1:])
        quantity = slave_bag.split(" ")[0]
        slave_bags.append((bag, quantity))
    bags_map[master_bag] = slave_bags


def count_bag_colors(bags_map):
    bag_colors = set()

    def bags_walk(master_bag, target_bag):
        if master_bag == target_bag:
            return True
        target_bag_found = False
        for pair in bags_map[master_bag]:
            slave_bag = pair[0]
            if bags_walk(slave_bag, target_bag):
                target_bag_found = True
                bag_colors.add(master_bag)
        return target_bag_found

    target_bag = "shiny gold"
    for master_bag in bags_map:
        if bags_walk(master_bag, target_bag):
            bag_colors.add(master_bag)

    return len(bag_colors - set([target_bag]))


print(count_bag_colors(bags_map))
