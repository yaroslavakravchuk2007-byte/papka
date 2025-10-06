def wrap_in_tag(text, tag):
    valid_tags = {"a", "abbr", "b", "body", "caption", "cite", "code", "div", "form",
                  "h1", "h2", "h3", "h4", "h5", "h6", "header", "i", "s"}
    if tag in valid_tags:
        return f"<{tag}>{text}</{tag}>"
    else:
        return "Введён неверный тег"

html_code = wrap_in_tag("botay", "h5")

with open("test.html", "w", encoding="utf-8") as f:
    f.write(f"<html><body>{html_code}</body></html>")

print("Файл test.html создан. Открой его в браузере!")


