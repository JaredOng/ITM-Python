# NON-INTERACTIVE CODE CELL. YOU MAY RUN THIS CELL, BUT DO NOT EDIT IT.
# FOR DEMONSTRATION PURPOSES ONLY. DO NOT EDIT.

products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

# CODE CELL
# PROBLEM 1

def get_product(code):
    return products[code]
    
get_product("espresso")

# CODE CELL
# PROBLEM 2

def get_property(code, property):
    return products[code][property]
    
get_property("espresso", "price")

# CODE CELL
# PROBLEM 3

def main():
    f = open("receipt.txt", "w")
    while True:
        order = input("")
        if order == "/":
            subtotal = 0
            f.write("==\nCODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL\n")
            for menuitems in products.keys():
                if get_product(menuitems).setdefault("amount", 0) != 0:
                    f.write(menuitems + "\t\t"+ get_property(menuitems, "name") + "\t\t" + str(get_property(menuitems, "amount")) + "\t\t\t\t\t" +  str(get_property(menuitems, "price") * get_property(menuitems, "amount")) + "\n")
                    subtotal += get_property(menuitems, "price") * get_property(menuitems, "amount")
            f.write("Total:\t\t\t\t\t\t\t\t\t\t\t\t" + str(subtotal) + "\n==")
            break
        elif not("," in order):
            print("Invalid format")
            continue
        elif order.split(",")[0] in products.keys():
            get_product(order.split(",")[0]).setdefault("amount", 0)
            get_product(order.split(",")[0])["amount"] += int(order.split(",")[1])
        else:
            print("Invalid product")

            
            
main()