import csv
import json
import argparse

def main(inputfile, output):
    subreddit_to_count = dict()
    total = 0
    with open(inputfile) as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            sub = row[0]
            total = total + 1
            if sub in subreddit_to_count:
                subreddit_to_count[sub] = subreddit_to_count[sub] + 1
            else:
                subreddit_to_count[sub] = 1

    top200 = sorted(subreddit_to_count.items(), key=lambda x: x[1], reverse=True)[:200]
    json_list = map(lambda x: {"name":x[0], "size":x[1], "percent":(float(x[1])/total)}, top200)

    with open(output, "wb") as jsonfile:
        jsonfile.write(json.dumps(json_list))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("inputfile", help="input file")
    parser.add_argument("output", help="output file")

    args = parser.parse_args()

    main(args.inputfile, args.output)