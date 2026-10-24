#analysis of the effectiveness of an advertising company
print("Advertising analysis system")

#Data input
print("Please enter the following data:\n")
ad_spend=float(input("Ad spend ($):\n"))
clicks=int(input("Number of clicks:\n"))
purchases=int(input("Number of purchases:\n"))
average_order_value=float(input("Average order value ($): \n"))

if ad_spend==0:
  print("Error. Ad spend cannot be zero. \n ")

else:
    #Calculations (metrics)
    revenue=purchases*average_order_value
    profit=revenue-ad_spend
    roi=profit/ad_spend*100

    #Reporting
    print("\n ---Report---")
    print(f"Total revenue: ${revenue:.2f}\n")
    print(f"Net profit: ${profit:.2f}\n")
    print(f"ROI: {roi:.2f}%\n")

    #Business Verdict
    if roi>0: 
      print("VERDICT: Campaign is SUCCESSFUL! Recommend scaling up the budget \n")

    elif roi<0:
      print("VERDICT: Campaign is LOSS-MAKING! Recommend stopping immediately. \n ")

    elif roi==0:
      print("VERDICT: Break-even. Need to optimize targeting settings. \n")

    
