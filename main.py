import json

filename = "posts.json"


def load_data(filename):
    with open(filename, encoding="utf-8") as f:
        data = json.load(f)
        return data

data = load_data(filename)

def get_tags(data):
    """Выводит список тэгов"""
    for dic_ in data:
        tags = []
        list_tag = dic_["content"].split()
        for word in list_tag:
            if word[0] == "#":
                tags.append(word)
        dic_["tags"] = tags
    return tags

print(type(get_tags(load_data(filename))))


def save_posts_to_json(filename, data):
    """Сохраняет новый список словарей в json файл"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)



save_posts_to_json(filename, get_tags(data))