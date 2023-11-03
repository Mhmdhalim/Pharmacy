import sys
import pandas as pd

# Check the CSV file
if len(sys.argv) != 2:
    sys.exit('There is not exist CSV file.')


list_of_drug = sys.argv[1]
type_of_drug = ['Tablet', 'Syrup', 'Drops', 'Supp', 'Eff', 'Amp', 'Cream', 'Jel']
Drugs = type_of_drug + ['All']

def main():
    n_services = welcome()
    if n_services == "1":
        read()
    elif n_services == "2":
        Update()
    elif n_services == "3":
        shortfalls()
    elif n_services == "4":
        show_types()

# To take the type of the service
def welcome():
    hi = "Welcome, How I can help you?"
    while True:
        services = input(
        hi
        + """
Please select the service number.
1 For read
2 For update quantity and add or remove drug
3 For shortfalls
4 For to show types
Service number : """)
        if services in ['1', '2', '3', '4']: 
            return services


def read():
    global Drugs
    df = pd.read_csv(list_of_drug).sort_values(by='Type')
    pd.set_option('display.max_rows', df.shape[0]) 
    df = df.set_index('Name')

    while True:
        type = input(
        """
What type of drug you want to see?
Type : """).title()
        
        if type in Drugs:
            break
        else:
            print("It's not exist.")
    # ALL DRUGS
    if type == "All":
        print(df)
        while True:
            specific_service = input(
"""
Do you need other stastics?
Please choose number or write no.
1 for action
2 for quantity
Number : """).lower()
            if specific_service in ['1', '2', 'no']:
                break
    
        if specific_service == '1':
            print(df[["Action"]])
            Check()
        elif specific_service == '2':
            print(df[["Quantity"]])
            Check()
        elif specific_service == "no":
            sys.exit()

    # SYRUP
    if type == "Syrup":
        filt = df["Type"] == "syrup"
        while True:
            specific_service = input(
"""
Do you need other stastics?
Please choose number or write no.
1 for all
2 for action
3 for quantity
Number : """).lower()
            if specific_service in ['1', '2', '3', 'no']:
                break
        
        if specific_service == '1':
            print(df.loc[filt])
            Check()
        elif specific_service == '2':
            print(df.loc[filt, ["Action"]])
            Check()
        elif specific_service == '3':
            print(df.loc[filt, ["Quantity"]])
            Check()
        elif specific_service == "no":
            sys.exit()
    # TABLET
    if type == "Tablet":
        filt = df["Type"] == "tablet"
        while True:
            specific_service = input(
"""
Do you need other stastics?
Please choose number or write no.
1 for all
2 for action
3 for quantity
Number : """).lower()
            if specific_service in ['1', '2', '3', 'no']:
                break
        if specific_service == '1':
            print(df.loc[filt])
            Check()
        elif specific_service == '2':
            print(df.loc[filt, ["Action"]])
            Check()
        elif specific_service == '3':
            print(df.loc[filt, ["Quantity"]])
            Check()
        elif specific_service == "no":
            sys.exit()
        
    # LOTION
    if type == "Drops":
        filt = df["Type"] == "drops"
        while True:
            specific_service = input(
"""
Do you need other stastics?
Please choose number or write no.
1 for all
2 for action
3 for quantity
Number : """).lower()
            if specific_service in ['1', '2', '3', 'no']:
                break
        if specific_service == '1':
            print(df.loc[filt])
            Check()
        elif specific_service == '2':
            print(df.loc[filt, ["Action"]])
            Check()
        elif specific_service == '3':
            print(df.loc[filt, ["Quantity"]])
            Check()
        elif specific_service == "no":
            sys.exit()
    # CREAM
    if type == "Cream":
        filt = df["Type"] == "cream"
        while True:
            specific_service = input(
"""
Do you need other stastics?
Please choose number or write no.
1 for all
2 for action
3 for quantity
Number : """).lower()
            if specific_service in ['1', '2', '3', 'no']:
                break
        if specific_service == '1':
            print(df.loc[filt])
            Check()
        elif specific_service == '2':
            print(df.loc[filt, ["Action"]])
            Check()
        elif specific_service == '3':
            print(df.loc[filt, ["Quantity"]])
            Check()
        elif specific_service == "no":
            sys.exit()
    # GEL
    if type == "Jel":
        filt = df["Type"] == "jel"
        while True:
            specific_service = input(
"""
Do you need other stastics?
Please choose number or write no.
1 for all
2 for action
3 for quantity
Number : """).lower()
            if specific_service in ['1', '2', '3', 'no']:
                break
        if specific_service == '1':
            print(df.loc[filt])
            Check()
        elif specific_service == '2':
            print(df.loc[filt, ["Action"]])
            Check()
        elif specific_service == '3':
            print(df.loc[filt, ["Quantity"]])
            Check()
        elif specific_service == "no":
            sys.exit()
    # SUPPOSITORY
    if type == "Supp":
        filt = df["Type"] == "supp"
        while True:
            specific_service = input(
"""
Do you need other stastics?
Please choose number or write no.
1 for all
2 for action
3 for quantity
Number : """).lower()
            if specific_service in ['1', '2', '3', 'no']:
                break
        if specific_service == '1':
            print(df.loc[filt])
            Check()
        elif specific_service == '2':
            print(df.loc[filt, ["Action"]])
            Check()
        elif specific_service == '3':
            print(df.loc[filt, ["Quantity"]])
            Check()
        elif specific_service == "no":
            sys.exit()
    # AMP
    if type == "Amp":
        filt = df["Type"] == "AMP"
        while True:
            specific_service = input(
"""
Do you need other stastics?
Please choose number or write no.
1 for all
2 for action
3 for quantity
Number : """).lower()
            if specific_service in ['1', '2', '3', 'no']:
                break
        if specific_service == '1':
            print(df.loc[filt])
            Check()
        elif specific_service == '2':
            print(df.loc[filt, ["Action"]])
            Check()
        elif specific_service == '3':
            print(df.loc[filt, ["Quantity"]])
            Check()
        elif specific_service == "no":
            sys.exit()
    # EFFER
    if type == "Eff":
        filt = df["Type"] == "EFF"
        while True:
            specific_service = input(
"""
Do you need other stastics?
Please choose number or write no.
1 for all
2 for action
3 for quantity
Number : """).lower()
            if specific_service in ['1', '2', '3']:
                break
        if specific_service == '1':
            print(df.loc[filt])
            Check()
        elif specific_service == '2':
            print(df.loc[filt, ["Action"]])
            Check()
        elif specific_service == '3':
            print(df.loc[filt, ["Quantity"]])
            Check()
        else:
            sys.exit()


def Update():
    df = pd.read_csv(list_of_drug).sort_values(by='Type')
    pd.set_option('display.max_rows', df.shape[0]) 
    while True:
        Condition = input("""
Please choose what are you need? 
1 for addition
2 for update
3 for remove
Number : """)
        if Condition in ['1', '2', '3']:
            break
    # ADDITION
    if Condition == '1':
        Name = input("Name: ").lower()
        Type = input("Type: ").lower()
        Action = input("Action: ").lower()
        Quantity = input("Quantity: ")
        New_drug ={'Name': Name, 'Type': Type, 'Action': Action,'Quantity': Quantity}
        
        df = df._append(New_drug, ignore_index=True)
        df.to_csv(list_of_drug, index=False)
        Check()
    # UPDATER
    elif Condition == '2':
        Drug = input("Drug: ").lower()
        Quantity = int(input("Quantity: "))
        filt = df['Name'] == Drug
        df.loc[filt, 'Quantity'] = Quantity
        df.to_csv(list_of_drug, index=False)
        Check()
    # REMOVER
    elif Condition == '3':
        print(df.index)
        Name = input("Name: ").lower()
        df = df.drop(Name)
        df.to_csv(list_of_drug, index=False)
        Check()
    

def shortfalls():
    df = pd.read_csv(list_of_drug).sort_values(by='Type')
    pd.set_option('display.max_rows', df.shape[0]) 
    df = df.set_index('Name')
    
    while True:
        How = input('Do you need shortfalls according to Quantity or action or both? ').lower()
        if How in ['quantity', 'action', 'both']:
            break

    
    if How == 'quantity':
        type0 = input("Type of drug ? ")
        n = int(input("what is number of quantity do you need determine? "))
        filt = ((df['Quantity'] <= n) & (df['Type'] == type0))
        print(df.loc[filt])
        Check()
    elif How == 'action':
        type0 = input("Type of drug ? ")
        action = input("what is number of action do you need determine? ")
        filt = ((df['action'] == action) & (df['Type'] == type0))
        print(df.loc[filt])
        Check()
    elif How == 'both':
        type0 = input("Type of drug ? ")
        n = int(input("what is number of quantity do you need determine? "))
        action = input("what is number of action do you need determine? ")
        filt = ((df['Quantity'] <= n) & (df['Type'] == type0) & ((df['action'] == action)))
        print(df.loc[filt])
        Check()


def show_types():
    global type_of_drug
    print(*type_of_drug, sep='\n')
    main()


def Check():
    Y_N = input("""
Do you need anything else? """)
    if Y_N == 'yes' or Y_N == 'y':
        main()
    else:
        sys.exit()
    
if __name__ == "__main__":
    main()