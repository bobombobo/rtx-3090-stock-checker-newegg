import requests
import time
from colorama import Fore, Back, Style
import os
from time import sleep
#evgartx3090_newegg_url=("https://www.newegg.com/zotac-geforce-gt-730-zt-71116-10l/p/1FT-000M-002N0?Description=gtx%20730&cm_re=gtx_730-_-1FT-000M-002N0-_-Product")


def menutext():
    print("""
  
██████╗░████████╗██╗░░██╗  ██████╗░░█████╗░░█████╗░░█████╗░
██╔══██╗╚══██╔══╝╚██╗██╔╝  ╚════██╗██╔══██╗██╔══██╗██╔══██╗
██████╔╝░░░██║░░░░╚███╔╝░  ░█████╔╝██║░░██║╚██████║██║░░██║
██╔══██╗░░░██║░░░░██╔██╗░   ░╚═══██╗██║░░██║░╚═══██║██║░░██║
██║░░██║░░░██║░░░██╔╝╚██╗  ██████╔╝╚█████╔╝░█████╔╝╚█████╔╝
╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝  ╚═════╝░░╚════╝░░╚════╝░░╚════╝░

░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
  
By boboMbobo
https://github.com/bobombobo  
v0.0.1 (Highly unoptomized)
Thanks for using!
  """)
#i probs should've just createda list of links to check, for each link, i check the links if they contain out of stock or in stock, and if they do ill add that to a list of valid urls)

os.system('clear')


def counter():
    count = 15
    while count != 0:
        print("Till next refresh: " + str(count))
        sleep(1)
        count = count - 1
        print("\033[A                             \033[A")


def refresh():
  os.system('clear')
  menutext()
  start_time = time.time()
  Script()
  print("Time it took to check: " +str(time.time() - start_time))
  counter()


def Script():

    print(Fore.WHITE + "--------------------------")

    out_of_stock_cout = 0
    in_stock_count = 0
    error_count = 0
    instock_url_list = []

    evgartx3090_newegg_url = (
        "https://www.newegg.com/evga-geforce-rtx-3090-24g-p5-3987-kr/p/N82E16814487526?Description=rtx%203090&cm_re=rtx_3090-_-14-487-526-_-Product"
    )

    evgartx3090_neweggR = requests.get(evgartx3090_newegg_url).text

    if ("OUT OF STOCK") in evgartx3090_neweggR:
        print(
            Fore.RED +
            "out of stock of: EVGA GeForce RTX 3090 FTW3 ULTRA GAMING Video Card, 24G-P5-3987-KR, 24GB GDDR6X, iCX3 Technology, ARGB LED, Metal Backplate"
        )
        out_of_stock_cout = out_of_stock_cout + 1
    elif ("In stock") in evgartx3090_neweggR:
        print(
            Fore.GREEN +
            "in stock of: EVGA GeForce RTX 3090 FTW3 ULTRA GAMING Video Card, 24G-P5-3987-KR, 24GB GDDR6X, iCX3 Technology, ARGB LED, Metal Backplate"
        )
        instock_url_list.append(evgartx3090_newegg_url)
        in_stock_count = in_stock_count + 1
    else:
        print("Error")
        error_count = error_count + 1

    print(Fore.WHITE + "--------------------------")

    msirtx3090_newegg_url = (
        "https://www.newegg.com/msi-geforce-rtx-3090-rtx-3090-gaming-x-trio-24g/p/N82E16814137595?Description=rtx%203090&cm_re=rtx_3090-_-14-137-595-_-Product"
    )
    msirtx3090_neweggr = requests.get(msirtx3090_newegg_url).text
    if ("OUT OF STOCK") in msirtx3090_neweggr:
        print(
            Fore.RED +
            "out of stock of: MSI GeForce RTX 3090 DirectX 12 RTX 3090 GAMING X TRIO 24G 24GB 384-Bit GDDR6X PCI Express 4.0 HDCP Ready SLI Support Video Card"
        )
        out_of_stock_cout = out_of_stock_cout + 1
    elif ("In stock") in msirtx3090_neweggr:
        print(
            Fore.GREEN +
            "in stock of: MSI GeForce RTX 3090 DirectX 12 RTX 3090 GAMING X TRIO 24G 24GB 384-Bit GDDR6X PCI Express 4.0 HDCP Ready SLI Support Video Card"
        )
        instock_url_list.append(msirtx3090_newegg_url)
        in_stock_count = in_stock_count + 1
    else:
        print("Error")
        error_count = error_count + 1

    print(Fore.WHITE + "--------------------------")
    zotactrinityrtx3090_newegg_url = (
        "https://www.newegg.com/zotac-geforce-rtx-3090-zt-a30900d-10p/p/N82E16814500503?Description=rtx%203090&cm_re=rtx_3090-_-9SIANCVDU88863-_-Product"
    )

    zotactrinityrtx3090_neweggr = requests.get(
        zotactrinityrtx3090_newegg_url).text

    if ("OUT OF STOCK") in zotactrinityrtx3090_neweggr:
        print(
            Fore.RED +
            "out of stock of: MSI GeForce RTX 3090 DirectX 12 RTX 3090 GAMING X TRIO 24G 24GB 384-Bit GDDR6X PCI Express 4.0 HDCP Ready SLI Support Video Card"
        )
        out_of_stock_cout = out_of_stock_cout + 1
    elif ("In stock" in zotactrinityrtx3090_neweggr):
        print(
            Fore.GREEN +
            "in stock of: ZOTAC GAMING GeForce RTX 3090 Trinity 24GB GDDR6X 384-bit 19.5 Gbps PCIE 4.0 Gaming Graphics Card, IceStorm 2.0 Advanced Cooling, SPECTRA 2.0 RGB Lighting, ZT-A30900D-10P"
        )
        instock_url_list.append(zotactrinityrtx3090_newegg_url)
        in_stock_count = in_stock_count + 1
    else:
        print("Error")
        error_count = error_count + 1
    #  print("Price: " + )

    print(Fore.WHITE + "--------------------------")

    msirtx3090_SUPRIM_url = (
        "https://www.newegg.com/msi-geforce-rtx-3090-rtx3090-suprim-x-24g/p/N82E16814137610?Description=rtx%203090&cm_re=rtx_3090-_-14-137-610-_-Product"
    )

    msirtx3090_SUPRIMr = requests.get(msirtx3090_SUPRIM_url).text

    if ("OUT OF STOCK") in msirtx3090_SUPRIMr:
        print(
            Fore.RED +
            "out of stock of: MSI GeForce RTX 3090 RTX 3090 SUPRIM X 24G 24GB 384-Bit GDDR6X Video Card"
        )
        out_of_stock_cout = out_of_stock_cout + 1
    elif ("In stock" in msirtx3090_SUPRIMr):
        print(
            Fore.GREEN +
            "in stock of: MSI GeForce RTX 3090 RTX 3090 SUPRIM X 24G 24GB 384-Bit GDDR6X Video Card"
        )
        instock_url_list.append(msirtx3090_SUPRIM_url)

        in_stock_count = in_stock_count + 1
    else:
        print("Error")
        error_count = error_count + 1

    print(Fore.WHITE + "--------------------------")

    asusrtx3090_gaming_newegg_url = (
        "https://www.newegg.com/asus-geforce-rtx-3090-tuf-rtx3090-o24g-gaming/p/N82E16814126454?Description=rtx%203090&cm_re=rtx_3090-_-14-126-454-_-Product"
    )

    asusrtx3090_gaming_neweggr = requests.get(
        asusrtx3090_gaming_newegg_url).text

    if ("OUT OF STOCK") in msirtx3090_SUPRIMr:
        print(
            Fore.RED +
            "out of stock of: ASUS TUF Gaming GeForce RTX 3090 DirectX 12 TUF-RTX3090-O24G-GAMING 24GB 384-Bit GDDR6X PCI Express 4.0 x16 HDCP Ready SLI Support Video Card"
        )
        out_of_stock_cout = out_of_stock_cout + 1
    elif ("In stock" in msirtx3090_SUPRIMr):
        print(
            Fore.GREEN +
            "in stock of: ASUS TUF Gaming GeForce RTX 3090 DirectX 12 TUF-RTX3090-O24G-GAMING 24GB 384-Bit GDDR6X PCI Express 4.0 x16 HDCP Ready SLI Support Video Card"
        )
        instock_url_list.append(asusrtx3090_gaming_newegg_url)

        in_stock_count = in_stock_count + 1
    else:
        print("Error")
        error_count = error_count + 1

    print(Fore.WHITE + "--------------------------")

    asusrtx3090_rog_newegg_url = ("https://www.newegg.com/asus-geforce-rtx-3090-rog-strix-rtx3090-o24g-gaming/p/N82E16814126456?Description=rtx%203090&cm_re=rtx_3090-_-14-126-456-_-Product")

    asusrtx3090_rog_neweggr = requests.get(
        asusrtx3090_rog_newegg_url).text

    if ("OUT OF STOCK") in asusrtx3090_rog_neweggr:
        print(
            Fore.RED +
            "out of stock of: ASUS ROG Strix GeForce RTX 3090 DirectX 12 ROG-STRIX-RTX3090-O24G-GAMING 24GB 384-Bit GDDR6X PCI Express 4.0 x16 HDCP Ready SLI Support Video Card"
        )
        out_of_stock_cout = out_of_stock_cout + 1
    elif ("In stock" in asusrtx3090_rog_neweggr):
        print(
            Fore.GREEN +
            "in stock of: ASUS ROG Strix GeForce RTX 3090 DirectX 12 ROG-STRIX-RTX3090-O24G-GAMING 24GB 384-Bit GDDR6X PCI Express 4.0 x16 HDCP Ready SLI Support Video Card"
        )
        instock_url_list.append(asusrtx3090_rog_newegg_url)

        in_stock_count = in_stock_count + 1
    else:
        print("Error")
        error_count = error_count + 1

    print(Fore.WHITE + "---------------------------------------------------------------")


    #print(Fore.MAGENTA + "-------------------------------------------")

    #print("")
    print(Fore.RED + "--------------------------")
    print("out of stock count: " + str(out_of_stock_cout))
    print(Fore.RED + "--------------------------")
    print(Fore.GREEN + "--------------------------")
    print("in stock count: " + str(in_stock_count))
    instock_url_list_fix = str(instock_url_list)
    print(Fore.GREEN+"Urls of video cards in stock: " + str(instock_url_list_fix))
    print(Fore.GREEN + "--------------------------")
    print(Fore.WHITE + "Errors: " + str(error_count))
    print("Links checked: " + str(out_of_stock_cout + in_stock_count + error_count))
    if error_count != 0:
        print("Awwwwwww! Refreshing script to try to resolve the error!")
        sleep(3)
        refresh()
    


while True:
    refresh()
