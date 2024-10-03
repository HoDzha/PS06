# Импортируем модуль со временем
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация драйвера
driver = webdriver.Firefox()
url = "https://www.divan.ru/ufa/category/svet"
driver.get(url)

# Пауза для загрузки страницы
time.sleep(3)

# Собираем данные о светильниках
products = driver.find_elements(By.CLASS_NAME, 'lsooF')  # Элемент карточки товара

data = []
print(products)
# driver.quit()

# Цикл по всем элементам на странице
for product in products:
    try:
        # Название светильника
 #       name = product.find_element(By.CLASS_NAME, 'item__title').text
        name = product.find_element(By.CSS_SELECTOR, "span[itemprop='name']").text

        # Цена светильника
        price = product.find_element(By.CSS_SELECTOR, "meta[itemprop='price']").get_attribute("content")

        # Ссылка на продукт
        link = product.find_element(By.CSS_SELECTOR, "link[itemprop='url']").get_attribute('href')

        data.append([name, price, link])
    except Exception as e:
        print(f"Ошибка при обработке элемента: {e}")

# Закрываем браузер
driver.quit()

# Запись данных в CSV файл

with open('result.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Название", "Цена", "Ссылка"])  # Заголовки столбцов
    writer.writerows(data)

print("Данные успешно выгружены в result.csv")

