# not working right - need to fix something...
# python script written to solve jindosh riddle
# TODO: OCR Detection would be cool

main_text = ""
with open("main.txt","r") as file:
    main_text = file.read()
    print(main_text)

# some threads on the internet claim that this order is irrelevant - so i am removing it from the string
main_text = main_text.replace("""At the dinner party were Lady Winslow, Doctor Marcolla, Countess Contee, Madam Natsiou, and Baroness Finch.""", "")

# some threads on the internet claim that this order is irrelevant - so i am removing it from the string
main_text = main_text.replace("""
In the morning, there were four heirlooms under the table: the Ring, Bird Pendant, the Snuff Tin, and the War Medal.
But who owned each?
""", "")

# print(main_text)

# not in any specefic order...
grills = ["Winslow", "Marcolla", "Natsiou", "Finch", "Contee"]
heirlooms = ["Ring",  "Bird", "Tin", "Medal", "Diamond"]

# match the girls/heirlooms with their order value
grills_orders = {}
heirlooms_orders = {}

# print(main_text)
for girl in grills:
    position = main_text.find(girl)
    grills_orders[position] = girl

for heirloom in heirlooms:
    position = main_text.find(heirloom)
    heirlooms_orders[position] = heirloom

# make it ordered
heirlooms_orders_sorted = sorted(heirlooms_orders.items())
grills_orders_sorted = sorted(grills_orders.items())

# print(heirlooms_orders_sorted)
# print(grills_orders_sorted)

# PS: Indexing start from 0
print(f"Lady Order: {grills_orders_sorted[1][1]}, {grills_orders_sorted[3][1]}, {grills_orders_sorted[4][1]}, {grills_orders_sorted[2][1]}, {grills_orders_sorted[0][1]}")
print(f"Heirloom Order: {heirlooms_orders_sorted[3][1]}, {heirlooms_orders_sorted[0][1]}, {heirlooms_orders_sorted[4][1]}, {heirlooms_orders_sorted[1][1]}, {heirlooms_orders_sorted[2][1]}")

#UNCOMMENT BELOW IF NOT WORKING -  TO UNDERTAND WHY..
print(heirlooms_orders_sorted)
print(grills_orders_sorted)
print(f"Lady Order: {grills_orders_sorted[1]}, {grills_orders_sorted[3]}, {grills_orders_sorted[4]}, {grills_orders_sorted[2]}, {grills_orders_sorted[0]}")
print(f"Heirloom Order: {heirlooms_orders_sorted[3]}, {heirlooms_orders_sorted[0]}, {heirlooms_orders_sorted[4]}, {heirlooms_orders_sorted[1]}, {heirlooms_orders_sorted[2]}")
# END

# this is the order according to multiple sources online and has always worked for me..
# 24531
# 41523
