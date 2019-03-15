class Limit:
    """docstring"""
    def __init__(self):
        self.order_book = {}
        self.order_count = 0
        self.asks = []  # contains orderId, sorted with respect to price
        self.bids = []  # contains orderId, sorted with respect to price

    def __getNewOrderId(self):
        self.order_count += 1
        return self.order_count

    @property
    def bbo(self):
        best = [None, None]
        if len(self.bids):
            best[0] = self.order_book[self.bids[-1]]["price"]
        if len(self.asks):
            best[1] = self.order_book[self.asks[0]]["price"]
        return best

    def add_limit_order(self, side, user_id, quantity, price):
        order_id = self.__getNewOrderId();
        order = {
            "side": side,
            "order_id": order_id,
            "user_id": user_id,
            "quantity": quantity,
            "price": price
            }
        self.order_book[order_id] = order
        if side == "ask":
            # heappush(self.asks, (order["price"], order_id))
            if not self.asks:
                self.asks.append(order_id)
            else:
                i = len(self.asks) - 1
                self.asks.append(0)
                while i >= 0 and self.order_book[self.asks[i]]["price"] > order["price"]:
                    self.asks[i + 1] = self.asks[i]
                    i -= 1
                self.asks[i + 1] = order_id
        elif side == "bid":
            # heappush(self.bids, (order["price"], order_id))
            if not self.bids:
                self.bids.append(order_id)
            else:
                i = len(self.bids) - 1
                self.bids.append(0)
                while i >= 0 and self.order_book[self.bids[i]]["price"] > order["price"]:
                    self.bids[i + 1] = self.bids[i]
                    i -= 1
                self.bids[i + 1] = order_id
        else:
            print("ERROR! Wrong side.")
        self.settle()

    def cancel_limit_order(self, order_id):
        if self.order_book[order_id]["side"] == 'ask':
            for i in range(len(self.asks)):
                if self.asks[i] == order_id:
                    del self.asks[i]
                    break
        else:
            for i in range(len(self.bids)):
                if self.bids[i] == order_id:
                    del self.bids[i]
                    break
        del self.order_book[order_id]

    def place_market_order(self, side, quantity):
        stock_count = 0
        stock_price = 0
        if side == "bid":
            i = len(self.bids) - 1  # since expensive bids are better
            while quantity != 0 and i >= 0:
                id = self.bids[-1]
                temp = self.order_book[id]["quantity"]
                if temp <= quantity:
                    quantity -= temp
                    stock_count += temp;
                    stock_price += temp * self.order_book[id]["price"]
                    self.cancel_limit_order(id)
                else:
                    self.order_book[id]["quantity"] -= quantity
                    stock_count += quantity
                    stock_price += quantity * self.order_book[id]["price"]
                    quantity = 0
                i -= 1
        elif side == "ask":
            i = 0
            while quantity != 0 and i < len(self.asks):
                id = self.asks[0]
                temp = self.order_book[id]["quantity"]
                if temp <= quantity:
                    quantity -= temp
                    stock_count += temp;
                    stock_price += temp * self.order_book[id]["price"]
                    self.cancel_limit_order(id)
                else:
                    self.order_book[id]["quantity"] -= quantity
                    stock_count += quantity
                    stock_price += quantity * self.order_book[id]["price"]
                    quantity = 0
                i += 1
            return [stock_count, stock_price / stock_count]

    def settle(self):
        while self.bids and self.asks and\
            self.order_book[self.bids[-1]]["price"] >= self.order_book[self.asks[0]]["price"]:
            order = {}
            if self.order_book[self.bids[-1]]["quantity"] > self.order_book[self.asks[0]]["quantity"]:
                order = self.order_book[self.asks[0]]
                self.cancel_limit_order(self.asks[0])
                self.place_market_order('bid', order["quantity"])
            elif self.order_book[self.bids[-1]]["quantity"] < self.order_book[self.asks[0]]["quantity"]:
                order = self.order_book[self.bids[-1]]
                self.cancel_limit_order(self.bids[-1])
                self.place_market_order('ask', order["quantity"])
            else:
                self.cancel_limit_order(self.asks[0])
                self.cancel_limit_order(self.bids[-1])

    # Printing functions
    def printOrder(self, order_id):
        print("\t{")
        for i in self.order_book[order_id]:
            if i == "side":
                continue
            print("\t\t", i, ':', self.order_book[order_id][i])
        print("\t},")

    def printBook(self):
        print("\nasks:[")
        for x in reversed(self.asks):
            self.printOrder(x)
        print("],")
        print("bids:[")
        for x in reversed(self.bids):
            self.printOrder(x)
        print("]\n")


if __name__ == "__main__":
    lob_example = Limit()
    lob_example.add_limit_order('ask', 'alice', 10, 100)
    lob_example.add_limit_order('ask', 'bob', 5, 90)
    lob_example.add_limit_order('bid', 'charles', 20, 85)
    lob_example.add_limit_order('bid', 'dave', 10, 80)
    print("Order book is:")
    lob_example.printBook()

    lob_example.add_limit_order('ask', 'eve', 10, 95)
    print("Order book is:")
    lob_example.printBook()

    lob_example.place_market_order('ask', 12)
    print("Order book is:")
    lob_example.printBook()

    lob_example.cancel_limit_order(3)
    print("Order book is:")
    lob_example.printBook()

    print("BBO is:")
    print(lob_example.bbo)
    print()

    print("Order book is:")
    lob_example.add_limit_order('bid', 'dave', 3, 95)
    lob_example.printBook()
