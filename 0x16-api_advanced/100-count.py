#!/usr/bin/python3
import requests
import json

def count_words(subreddit, word_list):
  """Counts the number of times each keyword appears in the titles of all hot articles for the given subreddit.

  Args:
    subreddit: The name of the subreddit to query.
    word_list: A list of keywords to search for.

  Returns:
    None.
  """

  url = "https://api.reddit.com/r/{}/hot?limit=25".format(subreddit)
  response = requests.get(url)
  if response.status_code != 200:
    return

  data = json.loads(response.content)
  titles = [post["title"] for post in data["data"]["children"]]

  keyword_counts = {}
  for title in titles:
    for word in word_list:
      word = word.lower()
      if word in title.lower():
        if word not in keyword_counts:
          keyword_counts[word] = 0
        keyword_counts[word] += 1

  sorted_keyword_counts = sorted(keyword_counts.items(), key=lambda x: (-x[1], x[0]))

  for word, count in sorted_keyword_counts:
    print("{}: {}".format(word, count))

  if data["data"]["after"]:
    count_words(subreddit, word_list, data["data"]["after"])


if __name__ == "__main__":
  subreddit = "python"
  word_list = ["python", "javascript"]
  count_words(subreddit, word_list)
