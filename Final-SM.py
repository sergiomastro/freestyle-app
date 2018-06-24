# worldcup results - Sergio Mastrogiovanni
#Check the results of the games, print them and write them into an excel file

import os
import csv
import pdb
import requests

# pdb.set_trace()



print("--------------------")
print("WORLD CUP 2018 - RESULTS:")
print("                         ")


r = requests.get('http://worldcup.sfg.io/matches').json()
m = ((m['home_team'], m['away_team']) for m in r if m['status'] == 'completed')



with open('Results.csv', 'w', newline='') as csvfile:
    fieldnames=['Country1','Goals1','Country2','Goals2']
    gamewriter = csv.DictWriter(csvfile,fieldnames=fieldnames)
    gamewriter.writerow({'Country1':'Country1','Goals1':'Goals1','Country2':'Country2','Goals2':'Goals2'})

#    thewriter=writerow(['col1','col2','col3'])
    for h, a in m:
        print(h['country'], h['goals'], 'x', a['country'], a['goals'])
        print("-------------------------")
        gamewriter.writerow({'Country1':h['country'],'Goals1':h['goals'],'Country2':a['country'],'Goals2': a['goals']})

"""
for h, a in m:
   print(h['country'], h['goals'], 'x', a['country'], a['goals'])
   print("-------------------------")
#   gamewriter.writerow(['Game', 'Country', 'Result'])

   with open(filepath, "r") as csv_file:
       writer = csv.DictReader(csv_file)
       all_sales = [float(row["sales price"]) for row in reader]
       monthly_sales = sum(all_sales)
       monthly_sales_usd = "${0:,.2f}".format(monthly_sales)
       print("... Total Sales: " + monthly_sales_usd)


with open('Results.csv', 'w', newline='') as csvfile:
    fieldnames=['col1','col2','col3']
    thewriter=csv.DictWriter(csvfile,fieldnames=fieldnames)

#    thewriter=writerow(['col1','col2','col3'])

    for i in range(1,100):
        thewriter.writerow({'col1':'one','col2':'two','col3':'three'})


"""
