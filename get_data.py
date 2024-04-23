import time
import json
import pandas as pd
from playwright.sync_api import sync_playwright


class GreetingParse():
    
    def __init__(self) -> None:
        self.url = "https://www.pozdravuha.ru/" # https://pozdravok.com/
        self.menus = ['.filters.menu-block.bg2.menu-left-main', '.filters.menu-block.bg3.menu-left-subrazd',
                      '.filters.menu-block.bg3.menu-left-subrazd']
        self.text = ['.item.pozdravuha_ru_text']

    def parse_menu(self, i: int) -> dict[str]:
        data = {} 
        menu = self.page.query_selector(self.menus[i])
        if menu:
            list_menu = menu.query_selector_all('a')
            for item in list_menu:
                item_menu = item.evaluate("""
                    el => ({
                        category: el.innerText,
                        link: el.href
                    })
                """)
                data[item_menu['category']] = item_menu['link']
        return data

    def count_pages(self) -> None:
        items = self.page.query_selector_all('.btn.btn-default.paginator_a')
       
        if items:
            return len(items) // 2 
        else:
            return 1

    def next_page(self) -> None:
        self.page.evaluate("""
            const elements = document.querySelectorAll('.btn.btn-default.paginator_a');
            const lastElement = elements[elements.length - 1];

            if (lastElement) {
                lastElement.click();
            }
        """)
        time.sleep(4)


    def parse_text(self, url: str, holiday: str, to: str, description: str) -> None:
        data = {'text': [], 'likes': [], 'holiday': [], 'to': [], 'description': []}

        self.page.goto(url=url, timeout=60000)
        time.sleep(2)
        '''проверяем количество страниц'''
        count_pages = self.count_pages()
        for _ in range(count_pages - 1):
            items = self.page.query_selector_all(self.text[0])
            for item in items:
                item = item.evaluate("""
                    el => {
                        let text = el.innerText.replace(/<br>/g, '\\n');
                        try{
                            text = text.replace(/© Принадлежит сайту\. Автор: .*?\\n/g, '');
                        } catch{}
                        text = text.replace(/Создать открытку *?/g, '');
                        // text = text.replace(/\d+/gm, '');
                        let likes = el.querySelector('.badge') ? el.querySelector('.badge').innerText : '';
                        return {
                            text: text.trim(),
                            likes: likes
                        };
                    }
                """)
                data['text'].append(item['text'])
                data['likes'].append(item['likes'])
                data['to'].append(to)
                data['description'].append(description)
                data['holiday'].append(holiday)
            df = pd.DataFrame(data)
            df.to_csv('data/greetings.csv', index=False, encoding='utf-8', mode='a+', header=False)
            self.next_page()

    def get_data(self) -> None:
        data_dict = self.parse_menu(i=0)
        for x in data_dict:
            self.page.goto(data_dict[x])
            time.sleep(2)
            data_dict[x] = self.parse_menu(i=1)
            if isinstance(data_dict[x], dict):
                for y in data_dict[x]:
                    self.page.goto(data_dict[x][y])
                    time.sleep(2)
                    data_dict[x][y] = self.parse_menu(i=2)
                    if data_dict[x][y]:
                        for z in data_dict[x][y]:
                            print('z: ' + z)
                            self.parse_text(url=data_dict[x][y][z], holiday=x, to=y, description=z) # здесь собираем данные
                            time.sleep(2)
                            print(f'{x}   {y}   {z} [+]')
                    else:
                        self.parse_text(url=self.page.url, holiday=x, to=y, description='') # здесь собираем данные
                        time.sleep(2)
                        print(f'{x}   {y} [+]')

    def parse(self):
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            self.context = browser.new_context()
            self.page = self.context.new_page()
            self.page.goto(self.url) 
            time.sleep(5)
            self.get_data_()

if __name__ == "__main__":
    GreetingParse().parse()