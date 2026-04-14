import requests
from bs4 import BeautifulSoup

class CurrencyConverter:
    def __init__(self):
        self.url = "https://bank.gov.ua/ua/markets/exchangerates"
        self.usd_rate = self._get_usd_rate()

    def _get_usd_rate(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            rows = soup.find_all('tr')
            
            for row in rows:
                if 'USD' in row.text:
                    cells = row.find_all('td')
                    rate_text = cells[-1].text.replace(',', '.')
                    return float(rate_text)
            
            raise ValueError("Неможливо знайти курс USD на сторінці.")
            
        except Exception as e:
            print(f"Помилка при парсингу: {e}")
            return None

    def convert_to_usd(self, amount_uah):
        if self.usd_rate:
            return amount_uah / self.usd_rate
        return None

def main():
    converter = CurrencyConverter()
    
    if converter.usd_rate is None:
        print("Не вдалося ініціалізувати конвертер.")
        return

    print(f"Актуальний курс долара (НБУ): {converter.usd_rate} UAH")
    
    try:
        amount = float(input("Введіть суму у гривнях (UAH): "))
        result = converter.convert_to_usd(amount)
        
        if result:
            print(f"Сума у ​​доларах США: {result:.2f} USD")
    except ValueError:
        print("Помилка: будь ласка, введіть числове значення.")

if __name__ == "__main__":
    main()