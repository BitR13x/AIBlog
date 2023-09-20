import os
import g4f
from g4f.Provider import You
from random import randint
from ast import literal_eval
import re

def remove_special_characters(input_string: str) -> str:
    pattern = r"[:'?!,_]"
    # Use the re.sub() function to replace matches with an empty string
    cleaned_string = re.sub(pattern, '', input_string)

    return cleaned_string

def Response(querry: str) -> str:
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": querry}],
        provider=You,
        stream=False
    )
    return response


# Multi providers
def generate_articles(list_of_articles: list[str]) -> dict:
    articles = dict()
    for name in list_of_articles:
        create_article = f"Give me a markdown article about {name}, start with introduction do not use any starting title"
        content = Response(create_article)

        if not name in articles.keys():
            articles[name] = content

    return articles


def generate_dates(length: int) -> list[str]:
    return [f"{randint(2018, 2023)}-{randint(1, 12)}-{randint(1, 30)}" for _ in range(length)] 


def generate_tags(article_list: list[str]) -> list[str]:
    querry = f"generate a two possible tags for an article names {article_list}, output example: [tag1 tag2]\n[tag1 tag2], do not greet and do not add anything, just replace these tags for generated and split these article tags with new line"
    tags = Response(querry).split("\n")
    print(type(tags), tags)
    
    if type(tags) != type([]):
        raise TypeError("Wrong type of data")
    
    return tags


def write_article(dates: list[str], tags: list[str], articles: dict) -> None:
    i = 0
    for name in articles.keys():
        # transform into lowercase and join string and open
        filename = '-'.join(name.split(' ')).lower()
        filename = remove_special_characters(name)

        header = "---\nlayout: post\n"
        absolute_path = os.path.abspath(__file__).replace(os.path.basename(__file__), "")
        with open(f"{absolute_path}_posts/{dates[i]+'-'+filename}.md", "w") as f:
            title = "'"+name+"'"
            header += f"title: {title}\n"
            header += f"tags: {tags[i]}\n"
            header += "---\n\n"
            content = header + articles[name]
            f.write(content)
        
        i += 1

if __name__ == "__main__":
    print("  Generating titles[*]\n")
    # generate better titles
    email = "" 
    password = ""

    if email and password: #and revChatGpt:
    # ChatGPT
        from revChatGPT.V1 import Chatbot
        number_of_articles = 10
        title_querry = f"generate me {number_of_articles} trending technical ideas for an articles, Answer only with format of python array: example: [article1, article2], do not split it into multiple arrays and do not greet"
        
        chatbot = Chatbot(config={
            "email": email,
            "password": password
        })
        for data in chatbot.ask(title_querry):
            response = data["message"]

        list_of_articles = literal_eval(response)
    else:
        list_of_articles = [
            "The Metaverse Revolution: How VR and AR Are Shaping the Future",
            "NFTs: From Digital Art to Real-World Applications",
            "5G and Edge Computing: Powering the Future of IoT",
            "Artificial Intelligence in Healthcare: Advancements and Challenges",
            "Quantum Machine Learning: Bridging the Gap Between Quantum Computing and AI",
            "The Dark Web: Unveiling the Hidden Layers of the Internet",
            "Robotic Process Automation (RPA) in Business: Streamlining Operations",
            "The Ethics of AI: Addressing Bias and Fairness in Machine Learning",
            "Zero Trust Security: Rethinking Network Security in the Digital Age",
            "The Green Tech Revolution: Sustainability and Innovation in Technology"
        ]

    #list_of_articles = generate_titles()

    print("  Generating tags[*]\n")
    tags = generate_tags(list_of_articles)

    print("  Generating articles[*]\n")
    # write into hashmap
    articles = generate_articles(list_of_articles)

    print("  Writing into file[*]\n")
    # write into file
    write_article(generate_dates(length=len(list_of_articles)), tags, articles)

    print("Done")