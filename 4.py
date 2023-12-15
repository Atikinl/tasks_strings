model = {"TE100-S5":
             {"product Title":"5-Port 10/100Mbps Fast Ethernet Switch",
"10/100Mbps":"5x",
              "Forearding Caracity": "1Gbps",
              "MAC adress entries": "2k",
              "Enclozure Material": "Plactic"},
         "TE100-S8":
             {"product Title": "9-Port 10/100Mbps Fast Ethernet Switch",
              "10/100Mbps": "8x",
              "Forearding Caracity": "1.6Gbps",
              "MAC adress entries": "2k",
              "Enclozure Material": "Plactic"},
         "TE100-S50g":
             {"product Title": "5-Port 10/100Mbps GREENnet Switch",
              "10/100Mbps": "5x",
              "Forearding Caracity": "1Gbps",
              "MAC adress entries": "1k",
              "Enclozure Material": "Metal Desktop"},
         "TE100-S80g":
             {"product Title": "9-Port 10/100Mbps GREENnet Switch",
              "10/100Mbps": "8x",
              "Forearding Caracity": "1.6Gbps",
              "MAC adress entries": "1k",
              "Enclozure Material": "Metal Desktop"},
         "TE100-S16g":
             {"product Title": "16-Port 10/100Mbps GREENnet Switch",
              "10/100Mbps": "16x",
              "Forearding Caracity": "3.2Gbps",
              "MAC adress entries": "8k",
              "Enclozure Material": "Metal Rackmount"},
         "TE100-S524":
             {"product Title": "24-Port 10/100Mbps GREENnet Switch",
              "10/100Mbps": "24x",
              "Forearding Caracity": "4.8Gbps",
              "MAC adress entries": "8k",
              "Enclozure Material": "Metal Rackmount"}
              }

for switch in model.keys():
    if model[switch]['10/100Mbps'] == "5x" and \
            model[switch]['MAC adress entries'] == "1k":
         print(model[switch])