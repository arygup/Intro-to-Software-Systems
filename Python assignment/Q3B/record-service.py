import csv

with open("./Record/2021113012-20-May-2022.csv", 'r') as file:
    F = csv.reader(file)
    d20 = []
    for row in F:
        d20.append(row)
with open("./Record/2021113012-21-May-2022.csv", 'r') as file:
    F = csv.reader(file)
    d21 = []
    for row in F:
        d21.append(row)
with open("./Record/2021113012-22-May-2022.csv", 'r') as file:
    F = csv.reader(file)
    d22 = []
    for row in F:
        d22.append(row)
with open("./Record/2021113012-23-May-2022.csv", 'r') as file:
    F = csv.reader(file)
    d23 = []
    for row in F:
        d23.append(row)
with open("./Record/2021113012-24-May-2022.csv", 'r') as file:
    F = csv.reader(file)
    d24 = []
    for row in F:
        d24.append(row)
with open("./Control/2021113012-controltable.csv", 'r') as file:
    F = csv.reader(file)
    control = []
    for row in F:
        control.append(row)

import sqlite3

mydb = sqlite3.connect('Record.db')
mycursor = mydb.cursor()
TickerRecord = """CREATE TABLE Ticker(
                'Date' VARCHAR(255),
                'Company Name' VARCHAR(255),
                'Industry' VARCHAR(255),
                'Previous Day Price' DECIMAL,
                'Current Price' DECIMAL,
                'Change in Price' DECIMAL(5, 2),
                'Confidence' VARCHAR(255)
                )"""
mycursor.execute(TickerRecord)
MetricsRecord = """CREATE TABLE Metrics(
                'KPIs' VARCHAR(255),
                'Metrics' VARCHAR(255)
                )"""
mycursor.execute(MetricsRecord)

insertTicker = """INSERT INTO Ticker VALUES (?, ?, ?, ?, ?, ?, ?)"""

v20 = []
for row in d20[1:]:
    v20.append(("20-05-2022", row[0], row[1],
                   "NULL", row[2], "Previous Day Not Listed", "Listed New"))
mycursor.executemany(insertTicker, v20)

v21 = []
for row in d21[1:]:
    for control_row in control:
        if row[1] == control_row[0]:
            if control_row[2] == "Low":
                L = float(control_row[1].strip('<>=% '))
            elif control_row[2] == "High":
                H = float(control_row[1].strip('<>=% '))
    for temp_row in d20:
        if row[0] == temp_row[0]:
            prev_price = float(temp_row[2])
    change_percent = (
        (float(row[2]) - float(prev_price)) / float(prev_price)) * 100
    if change_percent < L:
        confidence = "Low"
    elif (change_percent >= L) and (change_percent <= H):
        confidence = "Medium"
    else:
        confidence = "High"
    v21.append(("21-05-2022", row[0], row[1],
                   prev_price, row[2], change_percent, confidence))
mycursor.executemany(insertTicker, v21)

v22 = []
for row in d22[1:]:
    for control_row in control:
        if row[1] == control_row[0]:
            if control_row[2] == "Low":
                L = float(control_row[1].strip('<>=% '))
            elif control_row[2] == "High":
                H = float(control_row[1].strip('<>=% '))
    for temp_row in d21:
        if row[0] == temp_row[0]:
            prev_price = float(temp_row[2])
    change_percent = (
        (float(row[2]) - float(prev_price)) / float(prev_price)) * 100
    if change_percent < L:
        confidence = "Low"
    elif (change_percent >= L) and (change_percent <= H):
        confidence = "Medium"
    else:
        confidence = "High"
    v22.append(("22-05-2022", row[0], row[1],
                   prev_price, row[2], change_percent, confidence))
mycursor.executemany(insertTicker, v22)

v23 = []
for row in d23[1:]:
    for control_row in control:
        if row[1] == control_row[0]:
            if control_row[2] == "Low":
                L = float(control_row[1].strip('<>=% '))
            elif control_row[2] == "High":
                H = float(control_row[1].strip('<>=% '))
    for temp_row in d22:
        if row[0] == temp_row[0]:
            prev_price = float(temp_row[2])
    change_percent = (
        (float(row[2]) - float(prev_price)) / float(prev_price)) * 100
    if change_percent < L:
        confidence = "Low"
    elif (change_percent >= L) and (change_percent <= H):
        confidence = "Medium"
    else:
        confidence = "High"
    v23.append(("23-05-2022", row[0], row[1],
                   prev_price, row[2], change_percent, confidence))
mycursor.executemany(insertTicker, v23)

v24 = []
for row in d24[1:]:
    for control_row in control:
        if row[1] == control_row[0]:
            if control_row[2] == "Low":
                L = float(control_row[1].strip('<>=% '))
            elif control_row[2] == "High":
                H = float(control_row[1].strip('<>=% '))
    for temp_row in d23:
        if row[0] == temp_row[0]:
            prev_price = float(temp_row[2])
    change_percent = (
        (float(row[2]) - float(prev_price)) / float(prev_price)) * 100
    if change_percent < L:
        confidence = "Low"
    elif (change_percent >= L) and (change_percent <= H):
        confidence = "Medium"
    else:
        confidence = "High"
    v24.append(("24-05-2022", row[0], row[1],
                   prev_price, row[2], change_percent, confidence))
mycursor.executemany(insertTicker, v24)

industry_dict = {}

for row in v21:
    if industry_dict.get(row[2], 'NULL') == 'NULL':
        industry_dict[row[2]] = [0, 0]
    else:
        if row[-1] == "High":
            industry_dict[row[2]][0] += 1
        elif row[-1] == "Low":
            industry_dict[row[2]][1] += 1
for row in v22:
    if industry_dict.get(row[2], 'NULL') == 'NULL':
        industry_dict[row[2]] = [0, 0]
    else:
        if row[-1] == "High":
            industry_dict[row[2]][0] += 1
        elif row[-1] == "Low":
            industry_dict[row[2]][1] += 1
for row in v23:
    if industry_dict.get(row[2], 'NULL') == 'NULL':
        industry_dict[row[2]] = [0, 0]
    else:
        if row[-1] == "High":
            industry_dict[row[2]][0] += 1
        elif row[-1] == "Low":
            industry_dict[row[2]][1] += 1
for row in v24:
    if industry_dict.get(row[2], 'NULL') == 'NULL':
        industry_dict[row[2]] = [0, 0]
    else:
        if row[-1] == "High":
            industry_dict[row[2]][0] += 1
        elif row[-1] == "Low":
            industry_dict[row[2]][1] += 1
max_highs = -1
max_lows = -1
for industry in industry_dict:
    max_highs = max(max_highs, industry_dict[industry][0])
    max_lows = max(max_lows, industry_dict[industry][1])
for industry in industry_dict:
    if industry_dict[industry][0] == max_highs:
        b_ind = industry
    if industry_dict[industry][1] == max_lows:
        w_ind = industry

company_dict = {}

for row_20 in v20:
    for row_24 in v24:
        if row_20[1] == row_24[1]:
            gain = ((float(row_24[4]) - float(row_20[4])
                     ) / float(row_20[4])) * 100
            increment = float(row_24[4]) - float(row_20[4])
            loss = ((float(row_20[4]) - float(row_24[4])
                     ) / float(row_20[4])) * 100
            decrement = float(row_20[4]) - float(row_24[4])
            company_dict[row_20[1]] = [gain, increment, loss, decrement]

best_comps = []
worst_comps = []
max_gain = -1
max_loss = -1
for company in company_dict:
    max_gain = max(max_gain, company_dict[company][0])
    max_loss = max(max_loss, company_dict[company][2])
max_inc = -1
max_dec = -1
for company in company_dict:
    if company_dict[company][0] == max_gain:
        max_inc = max(max_inc, company_dict[company][1])
    if company_dict[company][2] == max_loss:
        max_dec = max(max_dec, company_dict[company][3])
for company in company_dict:
    if (company_dict[company][0] == max_gain) and (company_dict[company][1] == max_inc):
        best_comps.append(company)
    if (company_dict[company][2] == max_loss) and (company_dict[company][3] == max_dec):
        worst_comps.append(company)
best_comps.sort()
worst_comps.sort()
b_com = best_comps[0]
w_com = worst_comps[-1]
for company in company_dict:
    if company == b_com:
        bgain = str(company_dict[company][0])
    if company == w_com:
        wloss = str(company_dict[company][2])

val = [
    ("Best Listed Industry", b_ind),
    ("Best Company", b_com),
    ("Gain %", bgain),
    ("Worst Listed Industry", w_ind),
    ("Worst Company", w_com),
    ("Loss %", wloss)
]

insertMetrics = """INSERT INTO Metrics VALUES (?, ?)"""
mycursor.executemany(insertMetrics, val)
mydb.commit()
mydb.close()

