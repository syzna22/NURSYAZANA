'''
    Program purpose: To convert an amount in Malaysian Ringgit (MYR) to USD, EUR, GBP
    Programmer: NURSYAZANA BINTI MOHAMAD NOH EZAM
    Date: 7 February 2024
'''

print("Currency Conversion Program")
print (2 * "\n")

#Display exchange rates
print("Exchange Rates:")
print("USD - US Dollar: 0.25")
print("EUR - Euro: 0.21")
print("GBP - British Pound: 0.18")
print ("\n")
#Prompt the user to choose the target currency and choose the number
print("Choose the target currency:")
print("1. USD - US Dollar")
print("2. EUR - Euro")
print("3. GBP - British Pound")
print ("\n")
choice = int(input("Enter your choice (1-3): "))

#Prompt the user to input amount in MYR
amountMYR = float(input("Enter the amount in Malaysia Ringgit (MYR): "))

if choice == 1: #To calculate the target currency of USD
    convertusd = amountMYR * 0.25
    print("Equivalent amount in USD : ", convertusd)
elif choice == 2: #To calculate the target currency of EUR
    converteur = amountMYR * 0.21
    print("Equivalent amount in EUR : ", converteur)
elif choice == 3: #To calculate the target currency of GBP
    convertgbp = amountMYR * 0.18
    print("Equivalent amount in GBP : ", convertgbp)
else:
    print("Invalid option! Please re-enter number (1-3): ")



