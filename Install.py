import os
print("Welcome to the WINE installer")
output = input("Choose an OS, Debian or MacOS\n")
output = output.lower()
binForMac = "https://raw.githubusercontent.com/jakobneufeld/WineInstaller/master/Winery"

if output == "macos":
    print("Getting Binary")
    os.system("curl " + binForMac + " --output Wine" )
    print("Configuring")
    os.system("cp -f Wine /usr/local/bin/wine")
    os.system("chmod a+x /usr/local/bin/wine")
    print("A Sucess")
else :
    print("os not supported" + output)

