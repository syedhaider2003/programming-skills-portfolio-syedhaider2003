## CODELAB I ASSESSMENT 21 Utility App
## Vending Machine program using the Python programming language.
def vendingmachine():
#--------DRINKS-------#
a ={"item_no": "A1","item":"water","price":3.0,"stock":5}
b ={"item_no": "B2","item":"vimto","price":5.0,"stock":3}
c ={"item_no": "C3","item":"fanta","price":2.0,"stock":1}
d ={"item_no": "D4","item":"pepsi","price":1.0,"stock":2}
e ={"item_no": "E5","item":"dew","price":4.0,"stock":4}


#---------Snacks--------#

f ={"item_no": "F6","item":"lays","price":3.0,"stock":5}
g ={"item_no": "G7","item":"flute","price":3.0,"stock":5}
h ={"item_no": "H8","item":"biscof","price":3.0,"stock":5}
i ={"item_no": "I9","item":"chocalate","price":3.0,"stock":5}
j ={"item_no": "J10","item":"chips","price":3.0,"stock":5}

menu =(a,b,c,d,e,f,g,h,i,j)
Snacks=(f,g,h,i,j)
Drinks=(a,b,c,d,e)

print("""
██╗░░░██╗███████╗███╗░░██╗██████╗░██╗███╗░░██╗░██████╗░  ███╗░░░███╗░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗███████╗
██║░░░██║██╔════╝████╗░██║██╔══██╗██║████╗░██║██╔════╝░  ████╗░████║██╔══██╗██╔══██╗██║░░██║██║████╗░██║██╔════╝
╚██╗░██╔╝█████╗░░██╔██╗██║██║░░██║██║██╔██╗██║██║░░██╗░  ██╔████╔██║███████║██║░░╚═╝███████║██║██╔██╗██║█████╗░░
░╚████╔╝░██╔══╝░░██║╚████║██║░░██║██║██║╚████║██║░░╚██╗  ██║╚██╔╝██║██╔══██║██║░░██╗██╔══██║██║██║╚████║██╔══╝░░
░░╚██╔╝░░███████╗██║░╚███║██████╔╝██║██║░╚███║╚██████╔╝  ██║░╚═╝░██║██║░░██║╚█████╔╝██║░░██║██║██║░╚███║███████╗
░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝""")



#----Displayring ltems & prices in the vending machine-
def show (menu) :
# STOCK SYSTEM (DRINKS) for item in drinks:
for item in drinks:
if item.get('stock')== 0:
    drinks.remove(item)