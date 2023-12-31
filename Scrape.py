import requests
import re
import sys
import argparse
import json
from bs4 import BeautifulSoup
from tabulate import tabulate

def main():

    print(r"""

  ________  ______    _______        __         _______    _______
 /"       )/" _  "\  /"      \      /""\       |   __ "\  /"     "|
(:   \___/(: ( \___)|:        |    /    \      (. |__) :)(: ______)
 \___  \   \/ \     |_____/   )   /' /\  \     |:  ____/  \/    |
  __/  \\  //  \ _   //      /   //  __'  \    (|  /      // ___)_
 /" \   :)(:   _) \ |:  __   \  /   /  \\  \  /|__/ \    (:      "|
(_______/  \_______)|__|  \___)(___/    \___)(_______)    \_______)

    """)



    parser = argparse.ArgumentParser(
        prog = "Scrape",
        description="Scrapes websites for words and creates a custom password list")
    parser.add_argument("-l", default=5, type=int, help="Length of words to scrape")
    parser.add_argument("-u", default="https://scrapeme.live/shop/", help="full URL of webpage to scrape, example: 'http(s):www.example.com'")
    args = parser.parse_args()


    all_words = get_raw_text(args.u)
    word_count = top_words_from(all_words, args.l)


    top_words_dict = {}
    top_words_list = []

    for i in range(15):
        key, value = word_count[i]
        top_words_dict[key] = value
        top_words_list.append(key)


    with open("word_dump.txt", 'w') as dict_file:
        dict_file.write(json.dumps(top_words_dict))

    print("------------------------------------")
    print("The Top Words and Their Occurrences")
    print("------------------------------------")
    with open("word_dump.txt", "r") as file:
        reader = json.load(file)
        reader_list = [{'Word':key, 'Count': value} for key, value in reader.items()]
        print(tabulate(reader_list, headers="keys", tablefmt="fancy_grid"))



    new_list = letter_replacement(top_words_list)

    with open("rainbow.txt", "w") as file:
        for line in new_list:
            file.write(line)
            file.write("\n")

    print("\n")
    print("**************************************************************************************************")
    print("The custom password list is stored in a file called rainbow.txt in your current working directory")
    print("**************************************************************************************************" + "\n")
    print("A preview of the custom password list:")
    print("---------------------------------------")
    
    for password in new_list[:5]:
        print(password)


def get_html_of(url):

    resp = requests.get(url)

    if resp.status_code != 200:
        sys.exit(f"HTTP status code of {resp.status_code} returned, but 200 was expected. Exiting.")

    return resp.content.decode()

def count_occurrences(word_list,minimum_length):

    word_count= {}

    for word in word_list:
        if len(word) < minimum_length:
            continue
        if word not in word_count:
            word_count[word] = 1
        else:
            current_count = word_count.get(word)
            word_count[word] = current_count + 1

    return word_count

def get_raw_text(url):

    html = get_html_of(url)
    soup = BeautifulSoup(html, 'html.parser')
    raw_text = soup.get_text()

    return re.findall(r'\w+', raw_text)

def top_words_from(url,minimum_length):

    word_count = count_occurrences(url,minimum_length)

    return sorted(word_count.items(), key=lambda item: item[1], reverse=True)

def letter_replacement(list):
     updated_list = []
     for letter in list:
         word = letter.replace("s","$").replace("i","!").replace("a","@").replace("t","7").replace("e","3")
         updated_list.append(word)
     return updated_list


if __name__ == "__main__":
    main()

