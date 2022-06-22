import pandas as pd
lightonoff = pd.read_csv("./sample-timetable.csv")

lightonoff.loc[lightonoff['Lights'] == 'Yes', 'Y/n'] = "Yes"
lightonoff.loc[lightonoff['Lights'] != 'Yes', 'Y/n'] = "No"
print(lightonoff, end = '\n\n')
arrlightonoff = lightonoff.loc[:,"Y/n"].tolist()
for cell in arrlightonoff:
    if cell.lower() == "yes": print("LIGHT ON")
    else: print("Lights OUT")

arrDuration = lightonoff.loc[:,"Duration"].tolist()
for cellFloat in arrDuration:
    print(cellFloat)