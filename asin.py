from selenium import webdriver
import os

items = [
    "mobile",
    "laptop",
    "earphones",
    "bag",
    "mouse",
    "keyboard",
    "monitor",
    "box",
    "table",
    "chair",
    "file",
    "notebook",
    "pen",
    "pencil",
    "charger",
    "shirt",
    "jeans",
    "top",
    "trolley",
    "shampoo",
    "soap",
    "bucket",
    "blanket",
    "box",
    "mousepad",
    "napkin",
    "usb",
    "laptop cover",
    "skrew",
    "toolbox",
    "deo",
    "bottle",
    "watch",
    "scissors",
    "tape",
    "slippers",
    "belt",
    "leggings",
    "pants",
    "skirt",
    "shorts",
    "sweater",
    "jacket",
    "coat",
    "socks",
    "blazer",
    "switch board",
    "mop",
    "sofa",
    "teddy",
    "cork",
    "cards",
    "radio",
    "knife",
    "speakers",
    "pillow",
    "shoes",
    "eye liner",
]

result = []

for i in items:
    url = f"https://www.amazon.in/s?k={i}"

    driver = webdriver.Edge(
        r"C:\Users\vansh\Downloads\edgedriver_win64\msedgedriver.exe"
    )

    driver.get(url)

    link_elements = driver.find_elements_by_css_selector(
        ".a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal"
    )

    for link_element in link_elements:
        link = link_element.get_attribute("href")
        if link and "dp/" in link:
            result.append(link.split("dp/")[1].split("/")[0] + "\n")

    driver.quit()

with open("asin.txt", "a") as f:
    for i in set(result):
        f.write(i)


def remove_duplicate_words(text_file):
    unique_words = set()
    with open("asin.txt", "r") as f:
        for line in f:
            words = line.split()
            for word in words:
                unique_words.add(word)
        return list(unique_words)


text_file = "asin.txt"
unique_words = remove_duplicate_words(text_file)

with open("output.txt", "w") as f:
    for word in unique_words:
        f.write(word + "\n")

os.remove("asin.txt")
os.rename("output.txt", "asin.txt")
