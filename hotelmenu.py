#define the menu of restaurant
menu = {
    'Pizza':50,
    'Pasta':60,
    'Salad':70,
    'Coffee':80,
    'Lassi':100
}
#Greet
print("Wel come to my Coffee with Yes Bother")
print("Pizza:Rs 50\nPasta:Rs 60\nSalad:Rs 70\nCoffee: 80\nLassi: 100\n")

Order_total=0 

item_1 =input("Enter the name of iteam you want to order =")
if item_1 in menu:
    Order_total +=menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Odered item {item_1}is not available yet!")    
another_item =input("Do you want to add anotehr item?(Yes/No)")
if another_item =="Yes":
    item_2 = input ("Enter the name of second item =")
    if item_2 in menu: 
        Order_total +=menu[item_2]
        print(f"Item{item_2}has been added to order")
    else:
        print(f"Ordered item {item_2}is not available!")

print(f"The total amount of items to pay is {Order_total}")        

  




