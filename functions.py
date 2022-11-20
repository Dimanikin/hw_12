import json
import logging
from json import JSONDecodeError


def get_load_post():
    try:
        with open("posts.json", "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:

        return "File not found"

    except JSONDecodeError:
        logging.error("Json decode error")
        return "Json decode error"


def search_post(content):
    posts = get_load_post()
    found_posts = []
    for post in posts:
        if content.lower() in post["content"].lower():
            found_posts.append(post)
    logging.info(f"Выполняется поиск по слову {content}")
    return found_posts


def load_file(file, content):
    posts = get_load_post()
    post = {"pic": file, "content": content}
    posts.append(post)
    with open("posts.json", "w", encoding="utf-8") as f:
        return json.dump(posts, f, ensure_ascii=False, indent=2)
