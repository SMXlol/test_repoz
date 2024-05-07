class Pizzeria:
    def __init__(self):
        self.orders = []
        self.menu = {
            'Маргарита': 450,
            'Пепперони': 500,
            'Четыре сезона': 550,
            'Гавайская': 525
        }

    def take_order(self, order):
        total_cost = sum(self.menu[pizza] * quantity for pizza, quantity in order.items())
        self.orders.append(order)
        print(f"Заказ принят. Общая стоимость: {total_cost} руб.")
        return total_cost

    def process_order(self, order):
        # Место для реализации дополнительной логики обработки заказа
        print("Заказ готовится")

    def store_order_data(self, order):
        # Здесь данные заказа можно сохранять в базу данных или файл
        print("Данные о заказе сохранены")

class User:
    def __init__(self, name, address, payment_info):
        self.name = name
        self.address = address
        self.payment_info = payment_info

    def place_order(self, order, pizzeria):
        total_cost = pizzeria.take_order(order)
        self.handle_payment(total_cost)
        pizzeria.process_order(order)
        pizzeria.store_order_data(order)

    def handle_payment(self, amount):
        print(f"Сумма к оплате: {amount} руб.")
        paid_amount = int(input("Введите сумму, которой вы оплатите: "))
        if paid_amount < amount:
            print("Внесенная сумма меньше стоимости заказа, попробуйте снова.")
            self.handle_payment(amount)
        elif paid_amount > amount:
            change = paid_amount - amount
            print(f"Спасибо за оплату! Ваша сдача: {change} руб.")
        else:
            print("Спасибо за оплату!")

class DataStorage:
    def __init__(self):
        self.users_data = {}
        self.orders_data = {}

    def store_user_data(self, user):
        self.users_data[user.name] = user
        print(f"{user.name} забирайте заказ!")

    def store_order_data(self, order):
        self.orders_data[order.id] = order
        print("Заказ готов!")

    def retrieve_user_data(self, user_name):
        return self.users_data.get(user_name)

    def retrieve_order_data(self, order_id):
        return self.orders_data.get(order_id)

# Пример использования
pizzeria = Pizzeria()
user_name = input("Введите ваше имя: ")
user_address = input("Введите ваш адрес: ")
user_payment_info = input("Введите данные для оплаты: ")

print("Маргарита: 450\tПепперони: 500\tЧетыре сезона: 450\tГавайская: 525")

user = User(user_name, user_address, user_payment_info)
order = {}
order_active = True

while order_active:
    pizza_name = input("Введите название пиццы (или 'выход' для завершения заказа): ")
    if pizza_name.lower() == 'выход':
        order_active = False
    elif pizza_name in pizzeria.menu:
        quantity = int(input(f"Введите количество пицц {pizza_name}: "))
        if pizza_name in order:
            order[pizza_name] += quantity
        else:
            order[pizza_name] = quantity
    else:
        print("Извините, такой пиццы нет в меню. Попробуйте другую.")

if order:
    user.place_order(order, pizzeria)

data_storage = DataStorage()
data_storage.store_user_data(user)
