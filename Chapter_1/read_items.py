import csv

def read_items():
    """商品一覧のCSVデータを読み込んでタプルのジェネレータで返す
    各商品名は「商品名，価格」のタプルで返される
    """
    with open('./items.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            name = row[0]
            price = int(row[1])
            yield name, price

def is_addon_price(price):
    """価格が「買い合わせ対象商品」の場合Trueを返す
    """
    return price < 100

def main():
    items = read_items()
    print(items)
    for name, price in items:
        if is_addon_price(price):
            print(name)

if __name__ == "__main__":
    main()