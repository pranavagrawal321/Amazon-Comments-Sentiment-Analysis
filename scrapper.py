from requests_html import HTMLSession
import os


class Reviews:
    def __init__(self, asin):
        self.session = HTMLSession()
        self.asin = asin
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
        }
        self.url = f"https://www.amazon.in/product-reviews/{self.asin}/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews&sortBy=recent&pageNumber="

    def pagination(self, page):
        r = self.session.get(self.url + str(page))
        r.html.render(sleep=1)
        if not r.html.find("div[data-hook=review]"):
            return False
        else:
            return r.html.find("div[data-hook=review]")

    def parse(self, reviews):
        total = []
        for i in reviews:
            title_elem = i.find("a[data-hook=review-title]", first=True)
            rating_elem = i.find("i[data-hook=review-star-rating] span", first=True)
            body_elem = i.find("div.a-row.a-spacing-small.review-data", first=True)

            if title_elem is not None:
                title = title_elem.text.split("stars")[1]
            else:
                title = "N/A"

            if rating_elem is not None:
                rating = rating_elem.text
            else:
                rating = "N/A"

            if body_elem is not None:
                body = body_elem.text.replace("\n", " ")
            else:
                body = "N/A"

            data = {"title": title.strip(), "rating": rating, "body": body}

            total.append(data)

        return total


def main():
    with open("output_files/output_17.txt", "r") as f:
        asins = f.read().splitlines()

    new_folder = "amazon_reviews"
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)

    for asin in asins:
        r = Reviews(asin)
        csv_file = f"{new_folder}/{asin}_dataset.csv"
        with open(csv_file, "w", encoding="utf-8") as f:
            f.write("item,title,rating,body\n")
        for i in range(1, 6):
            reviews = r.pagination(i)
            if reviews:
                reviews_data = r.parse(reviews)
                with open(csv_file, "a", encoding="utf-8") as f:
                    for review in reviews_data:
                        f.write(
                            repr(asin)
                            + ","
                            + repr(review["title"])
                            + ","
                            + repr(review["rating"])
                            + ","
                            + repr(review["body"])
                            + "\n"
                        )

        print(f"Data for ASIN {asin} has been written to {csv_file}")


if __name__ == "__main__":
    main()
