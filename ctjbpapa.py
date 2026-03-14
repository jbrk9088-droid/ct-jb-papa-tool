import os
import platform

os.system("clear")

print("\033[1;32m")
print("""
 ██████╗████████╗        ██╗██████╗     ██████╗  █████╗ ██████╗  █████╗ 
██╔════╝╚══██╔══╝        ██║██╔══██╗    ██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║        ██║           ██║██████╔╝    ██████╔╝███████║██████╔╝███████║
██║        ██║      ██   ██║██╔═══╝     ██╔═══╝ ██╔══██║██╔═══╝ ██╔══██║
╚██████╗   ██║      ╚█████╔╝██║         ██║     ██║  ██║██║     ██║  ██║
 ╚═════╝   ╚═╝       ╚════╝ ╚═╝         ╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝

        CT JB PAPA TOOL
             v1.0
""")

print("Select From Menu\n")
print("1 : Tool Info")
print("2 : System Info")
print("3 : Update Tool")
print("4 : Exit")
print("5 : Whatsapp Ban")
print("6 : CT Group Tool")
print("7 : CT Bug Bot\n")

choice = input("Choice > ")

if choice == "1":
    print("\nCT JB PAPA Termux Tool")
    print("Owner : JB PAPA 71")

elif choice == "2":
    print("\nSystem Info:\n")
    print(platform.platform())

elif choice == "3":
    print("Updating Tool...")
    os.system("git pull")

elif choice == "4":
    exit()

elif choice == "5":
    print("Whatsapp Ban Tool Loading...")
    os.system("echo Feature coming soon")

elif choice == "6":
    print("CT Group Tool Running...")
    os.system("echo Feature coming soon")

elif choice == "7":
    print("CT Bug Bot Loading...")
    os.system("echo Feature coming soon")

else:
    print("Invalid option")
