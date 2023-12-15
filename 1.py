computers = {
    "pc1": {
        "os": "Windows 10",
        "processor": "ADM Phenom II",
        "ran": "8 Gb",
        "motherboard": "MSI87343",
        "hdd": "1Tb",
    },
    "pc2": {
        "os": "Windows 10",
        "processor": "ADM Phenom I",
        "ran": "4 Gb",
        "motherboard": "MSI845656",
        "hdd": "512Tb",
    },
    "pc3": {
        "os": "Windows 7",
        "processor": "ADM Phenom II",
        "ran": "8 Gb",
        "motherboard": "MSI87343",
        "hdd": "1Tb",
    },
}
device = input ("Введите имя устройства: ")
parameter = input("Введите имя параметра: ")

print(computers[device][parameter])