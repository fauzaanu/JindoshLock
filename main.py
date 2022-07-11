#
# python script written to solve jindosh riddle

# this is for testing purposes - user should be pasting the text to a main.txt file. In the final stage should build image recognition for ease of use - lets see...
main_text = """
At the dinner party were Lady Winslow, Doctor Marcolla, Countess Contee, Madam Natsiou, and Baroness Finch. The women sat in a row. They all wore different colors and Madam Natsiou wore a jaunty red hat. Baroness Finch was at the far left, next to the guest wearing a purple jacket. The lady in white sat left of someone in blue. I remember that white outfit because the woman spilled her wine all over it. The traveler from Dabokva was dressed entirely in green. When one of the dinner guests bragged about her Ring, the woman next to her said they were finer in Dabokva, where she lived.
So Lady Winslow showed off a prized Diamond, at which the lady from Karnaca scoffed, saying it was no match for her Snuff Tin. Someone else carried a valuable War Medal and when she saw it, the visitor from Dunwall next to her almost spilled her neighbor's whiskey. Countess Contee raised her beer in toast. The lady from Fraeport, full of absinthe, jumped up onto the table, falling onto the guest in the center seat, spilling the poor woman's rum. Then Doctor Marcolla captivated them all with a story about her wild youth in Baleton. In the morning, there were four heirlooms under the table: the Ring, Bird Pendant, the Snuff Tin, and the War Medal.
But who owned each?
"""

# some threads on the internet claim that this order is irrelevant - so i am removing it from the string
main_text = main_text.replace("""At the dinner party were Lady Winslow, Doctor Marcolla, Countess Contee, Madam Natsiou, and Baroness Finch.""", "")

# some threads on the internet claim that this order is irrelevant - so i am removing it from the string
main_text = main_text.replace("""
In the morning, there were four heirlooms under the table: the Ring, Bird Pendant, the Snuff Tin, and the War Medal.
But who owned each?
""", "")

#print(main_text)

grills = ["Winslow", "Marcolla", "Natsiou", "Finch", "Contee"]
heirlooms = ["Ring",  "Bird", "Tin", "Medal", "Diamond"]

grills_orders = {}
heirlooms_orders = {}
# print(main_text)
for girl in grills:
    position = main_text.find(girl)
    grills_orders[position] = girl

for heirloom in heirlooms:
    position = main_text.find(heirloom)
    heirlooms_orders[position] = heirloom

heirlooms_orders_sorted = sorted(heirlooms_orders.items())
grills_orders_sorted = sorted(grills_orders.items())

#print(heirlooms_orders_sorted)
#print(grills_orders_sorted)

print(f"Lady Order: {grills_orders_sorted[1][1]}, {grills_orders_sorted[3][1]}, {grills_orders_sorted[4][1]}, {grills_orders_sorted[2][1]}, {grills_orders_sorted[0][1]}")
print(f"Heirloom Order: {heirlooms_orders_sorted[3][1]}, {heirlooms_orders_sorted[0][1]}, {heirlooms_orders_sorted[4][1]}, {heirlooms_orders_sorted[1][1]}, {heirlooms_orders_sorted[2][1]}")

# this is the order
# 24531
# 41523
