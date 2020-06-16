import os
import re
import json
import sys
import datetime


def find_phrases():

    output = []
    files_count = 0
    regex = re.compile(r'seven day[s]? | 7-day[s]? | 7 day[s]? | free trial | trial key[s]? | 7 day[s]? try | '
                       r'try experience | trial experience | trial subscription', re.M | re.IGNORECASE)

    try:
        rootdir = sys.argv[1]
    except:
        print(f"A path must be provided as an argument.")
        sys.exit(1)

    if not os.path.exists('output_files'):
        os.mkdir('output_files')

    for folder, dirs, files in os.walk(rootdir):
        for file in files:
            if file.endswith('.md'):
                fullpath = os.path.join(folder, file)
                open_file = open(fullpath, 'r')
                text = open_file.read()
                matches = regex.findall(text)
                match_count = len(matches)

                if match_count != 0:
                    files_count += 1
                    output.append({'file': fullpath, 'match_count': match_count, 'matches': matches})
                open_file.close()

    print(f"Matched files: {files_count}")

    try:
        with open(f'output_files/output-{datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")}.json', 'w') as json_output:
            json.dump(output, json_output, sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ': '))
        print(f"Output saved: {json_output.name}")
    except:
        print(f"Something went wrong. Output was not written to file.")


if __name__ == "__main__":
    find_phrases()