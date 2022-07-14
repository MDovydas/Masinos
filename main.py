import sqlite3

connection = sqlite3.connect('cars.sqlite')
cursor = connection.cursor()


class Data:
    def __init__(self):
        self.make = input("Enter cars make: ")
        self.model = input("Enter cars model: ")
        self.color = input("Enter cars color: ")
        self.year = input("Enter cars year: ")
        self.price = input("Enter cars price: ")

    def new_row(self):
        cursor.execute("INSERT INTO CARS VALUES (?, ?, ?, ?, ?)",
                       (self.make, self.model, self.color, self.year, self.price))
        connection.commit()
        connection.close()
        return

    @staticmethod
    def search():
        make = input("Enter cars make: ") + "%"
        model = input("Enter cars model: ") + "%"
        color = input("Enter cars color: ") + "%"
        year_range_min = input("Enter years from: ")
        if year_range_min == "":
            year_range_min = "0"
        year_range_max = input("To: ")
        if year_range_max == "":
            year_range_max = "2030"
        price_range_min = input("Enter price from: ")
        if price_range_min == "":
            price_range_min = "0"
        price_range_max = input("To: ")
        if price_range_max == "":
            price_range_max = "50000"
        cursor.execute(
            """SELECT * 
            FROM CARS 
            WHERE make LIKE ? 
            AND model LIKE ? 
            AND color LIKE ? 
            AND YEAR BETWEEN ? AND ? 
            AND PRICE BETWEEN ? AND ?""",
            (make, model, color, year_range_min, year_range_max, price_range_min, price_range_max))
        results = cursor.fetchall()
        for result in results:
            print(result)
        return


class Menu:
    @staticmethod
    def menu():
        chose = int(input("Add to (1) or Search (2) Database ? \n(9) to exit\n"))
        if chose == 1:
            to_do = Data()
            to_do.new_row()
        elif chose == 2:
            Data.search()
        elif chose == 9:
            return quit()
        else:
            print("Wrong selection!\n")
        return


while True:
    Menu.menu()
