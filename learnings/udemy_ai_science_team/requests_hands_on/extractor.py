import requests


def run():
    for i in range(1, 11):
        url = f'https://quotes.toscrape.com/page/{i}'
        r = requests.get(url)
        html = r.text
        print(f'processing {url}')

        with open('resources/quotes', 'a', encoding="utf-8") as f:
            for line in html.split('\n'):
                if '<span class="text" itemprop="text">' in line:

                    line = line.replace('<span class="text" itemprop="text">', '').replace('</span>', '')
                    line = line.strip().replace('“', '').replace('”', '')
                    f.write(line)
                    f.write('\n')


if __name__ == '__main__':
    run()
