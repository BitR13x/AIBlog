## Technology

- [revChatGPT](https://github.com/acheong08/ChatGPT)
- [hamilton](https://github.com/zivong/jekyll-theme-hamilton)
- jekyll
- python
  - g4f
  - ast
  - re

## Getting Started

Follow these steps to get started with the Automatic Article Generator:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/BitR13x/AIBlog.git
   ```

2. **Generate Articles:**
   Login into chatgpt and use prompt to generate python list of article ideas:

```py
"generate me {number_of_articles} trending technical ideas for an articles, Answer only with format of python array: example: [article1, article2], do not split it into multiple arrays and do not greet"
```

and replace the variable: `list_of_articles` or you can use the revChatGPT library and place there email and password (not tested).

Then just launch the script and look into `_posts`.

```bash
python gen.py
```

3. **Hosting:**

One option is using gh-pages(github-pages)..
