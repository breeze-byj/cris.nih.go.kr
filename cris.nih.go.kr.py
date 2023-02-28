import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pySelenium import PySelenium


class Run(PySelenium):
    # 总页数62/
    def get_data(self):
        # 每页20行
        tr_number = 20
        # 每行20列
        td_number = 20
        table_all_list = []
        # 遍历table_tr
        for tr_num in range(1, tr_number + 1):
            print(f'打印第{tr_num}条数据')
            # 每一行的list
            table_info_list = []
            # 遍历table_td
            for td_num in range(2, td_number + 2):
                # 取每行数据
                table_info = (By.XPATH,
                              f'//*[@id="dataList"]/tr[{tr_num}]/td[{td_num}]')
                table_info = self.locator(table_info).text
                # 取到后保存在每一行的list中
                table_info_list.append(table_info)
            table_all_list.append(table_info_list)
            # print(table_info_list)
            # 调取写入函数,写入数据
        self.write_csv(table_all_list)

    # 写入函数
    def write_csv(self, data_list_name):
        with open('./data.csv', 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            for row in data_list_name:
                writer.writerow(row)

    ######> 点击culmns
    def culmns(self):
        culmns = (By.XPATH, '//*[@id="col_down"]')
        self.locator(culmns).click()
        # 选择
        for j in range(1, 15):
            cm = (By.XPATH, f'.//div[@class="sortlist clear"]/p[{j}]/input')
            self.locator(cm).click()
            time.sleep(1)
        # 关闭
        close = (By.XPATH, '//*[@id="div_view"]/div/div[3]/button')
        self.locator(close).click()

    ######> 翻页
    def turn_pages(self):
        for next_ in range(1, 8):
            for next in range(1, 11):
                time.sleep(0.5)
                # 下一页按钮
                if next_ == 1:
                    next_button = (By.XPATH, f'.//div[@class="paginate"]/a[{next}]')
                    self.locator(next_button).click()
                    time.sleep(5)
                else:
                    next_button = (By.XPATH, f'.//div[@class="paginate"]/a[{next + 2}]')
                    self.locator(next_button).click()
                    time.sleep(5)
                self.get_data()
            # 下10页
            next_10 = (By.XPATH, '//*[@id="paging"]/a[@title="next"]')
            self.locator(next_10).click()
            time.sleep(3)


if __name__ == '__main__':
    url = 'https://Y3Jpcy5uaWguZ28ua3I=/cris/search/listDetail.do?my_code=2308&intervention_type=&clinical_step=&search_yn=Y&class_yn=Y&class_title=Condition%28s%29%2FProblem%28s%29&class_title2=Neoplasms#1'
    browser = webdriver.Chrome()
    browser.implicitly_wait(20)
    start = Run(browser)
    # 打开url
    start.maxwin()
    start.visit_url(url)
    time.sleep(10)
    start.culmns()
    time.sleep(5)
    start.turn_pages()
    time.sleep(1)
