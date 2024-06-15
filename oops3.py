class shopping_cart:
    def __init__(self):
        self.item={}
    def add(self,item_n,price,quantity=1):
        if item_n in self.item:
            self.item[item_n]['quantity']+=quantity
        else:
            self.item[item_n]={'price':price,'quantity':quantity}
            print(f"added {quantity} of {item_n} to the cart")       
       
    def  remove(self,item_n,quantity=1):
        if item_n in self.item:
            if  self.item[item_n]['quantity']<=quantity:
                del self.item[item_n]
                print("items{item_n} is removed from the cart")
            else:
                self.item[item_n]['quantity']-=quantity
                print(f"removed all",item_n,"from the cart")
        else:
            print(f"{item_n} not found in the cart.")
            
                
            
            
            
            
            
            
    def total_price(self):
        total_price=0
        for item in self.item.values():
            total_price+=item['price']*item['quantity']
        return total_price
    
    def dispal_cart(self):
        if not self.item:
            print("the cart is empty.")
        else:
            print("shopping cart:")
            for item_n,details in self.item.items():
                print(f"{item_n}:{details['price']}x{details['quantity']}")
            print(f"Total: {self.total_price()}")
            
cart=shopping_cart()
cart.add("Apple",99,5)
cart.add("Banana",59,3)
cart.dispal_cart()

cart.remove("Apple",2)
cart.dispal_cart()

cart.add("Orange",29,2)
cart.dispal_cart()
cart.remove("Banana",3)
cart.dispal_cart()