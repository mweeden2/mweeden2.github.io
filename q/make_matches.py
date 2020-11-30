# Matt Weeden
# 11/30/2020

# This script generates matches for a secret santa drawing.

import argparse
import random
import uuid

def main():

    parser = argparse.ArgumentParser(description="This script generates matches for a secret santa drawing.")
    parser.add_argument("-v", "--verbose", help="be verbose about it", action="store_true")
    parser.add_argument("person_file", help="person file")
    args = parser.parse_args()


    ####################################################
    #
    ####################################################

    people = []
    with open(args.person_file, 'r') as f:
        for l in f:
            ls = l.split()
            people.append([ls[0], list(ls[1:])])

    to_be_given_a_person = list(people)
    to_be_given_to = [p[0] for p in people]

    matches = []

    for i in to_be_given_a_person:

        r = random.randint(0, len(to_be_given_to)-1)

        while to_be_given_to[r] in i[1]:
            if len(to_be_given_to) == 1:
                print("try again...")
                print()
                break
            r = random.randint(0, len(to_be_given_to)-1)

        matches.append([i[0], to_be_given_to[r]])
        to_be_given_to.remove(to_be_given_to[r])

    matches_with_uids = []

    for m in matches:
        matches_with_uids.append([m, uuid.uuid4()])

    print("uuids to share...")
    for i in matches_with_uids:
        print(i[0][0], "https://mweeden2.github.io/q/q=%s" % i[1])

    print("uuids to embed...")
    random.shuffle(matches_with_uids)
    for i in matches_with_uids:
        print(i[0][1], "%s" % i[1])



if __name__ == "__main__":
    main()
