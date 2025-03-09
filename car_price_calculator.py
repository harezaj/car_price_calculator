import pandas as pd
import numpy as np
import argparse
from datetime import datetime
import os

def calculate_max_affordable_price(max_monthly_payment=750, loan_term_months=60, 
                                 max_down_payment=20000, trade_in=6000,
                                 min_interest_rate=5.0, max_interest_rate=6.0, interest_step=0.5):
    """Calculate the maximum affordable car price based on financial parameters."""
    
    # Interest rates from max_interest_rate down by interest_step increments to min_interest_rate
    interest_rates = np.arange(max_interest_rate, min_interest_rate - 0.1, -interest_step)
    
    # Down payments starting from max_down_payment down by 5000 (ensuring it stays non-negative)
    down_payments = np.arange(max_down_payment, -1, -5000)
    
    # Create list for results (no pre-allocation in Python lists)
    max_affordable_cars = []
    
    for down_payment in down_payments:
        for interest_rate in interest_rates:
            for loan_amount in range(5000, 100000, 500):  # Incrementing loan amounts to find max affordable
                monthly_interest_rate = (interest_rate / 100) / 12
                if monthly_interest_rate > 0:
                    monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -loan_term_months)
                else:
                    monthly_payment = loan_amount / loan_term_months
    
                if monthly_payment > max_monthly_payment:
                    break  # Stop once we exceed the budget
    
                max_car_price = loan_amount + down_payment + trade_in
                max_affordable_cars.append([max_car_price, down_payment, interest_rate, loan_amount, monthly_payment])
    
    # Convert to DataFrame and sort by Max Car Price in descending order
    df_max_affordable = pd.DataFrame(max_affordable_cars, columns=['Max Car Price', 'Money Down', 'Interest Rate (%)', 'Loan Amount', 'Monthly Payment'])
    df_max_affordable = df_max_affordable.sort_values(by='Max Car Price', ascending=False)
    
    return df_max_affordable

def main():
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description='Calculate the maximum affordable car price based on your budget and preferences.')
    
    # Financial parameters
    parser.add_argument('--max_monthly', type=float, default=750, help='Maximum monthly payment')
    parser.add_argument('--loan_term', type=int, default=60, help='Loan term in months')
    parser.add_argument('--down_payment', type=float, default=20000, help='Maximum down payment')
    parser.add_argument('--trade_in', type=float, default=6000, help='Trade-in value')
    parser.add_argument('--min_rate', type=float, default=5.0, help='Minimum interest rate')
    parser.add_argument('--max_rate', type=float, default=6.0, help='Maximum interest rate')
    parser.add_argument('--interest_step', type=float, default=0.5, help='Interest rate step for calculations')
    
    args = parser.parse_args()
    
    # Calculate affordability
    print("Calculating maximum affordable car price based on your financial parameters...")
    df_affordable = calculate_max_affordable_price(
        max_monthly_payment=args.max_monthly,
        loan_term_months=args.loan_term,
        max_down_payment=args.down_payment,
        trade_in=args.trade_in,
        min_interest_rate=args.min_rate,
        max_interest_rate=args.max_rate,
        interest_step=args.interest_step
    )
    
    # Display affordability results
    print("\nTop 10 Affordable Car Price Options:")
    pd.set_option('display.precision', 2)  # Set display precision
    print(df_affordable.head(10))
    
    # Use the highest affordable price
    max_price = int(df_affordable['Max Car Price'].iloc[0])
    print(f"\nMaximum affordable car price: ${max_price:,}")
    
    # Display a summary of the financial parameters
    print("\nFinancial Parameters Summary:")
    print(f"Monthly Payment Budget: ${args.max_monthly}")
    print(f"Loan Term: {args.loan_term} months")
    print(f"Down Payment: ${args.down_payment:,}")
    print(f"Trade-in Value: ${args.trade_in:,}")
    print(f"Interest Rate Range: {args.min_rate}% - {args.max_rate}%")
    
    # Display the best option details
    best_option = df_affordable.iloc[0]
    print("\nBest Option Details:")
    print(f"Maximum Car Price: ${int(best_option['Max Car Price']):,}")
    print(f"Down Payment: ${int(best_option['Money Down']):,}")
    print(f"Trade-in Value: ${args.trade_in:,}")
    print(f"Loan Amount: ${int(best_option['Loan Amount']):,}")
    print(f"Interest Rate: {best_option['Interest Rate (%)']}%")
    print(f"Monthly Payment: ${best_option['Monthly Payment']:.2f}")

if __name__ == "__main__":
    main()

# HOW TO USE THIS SCRIPT:
# -----------------------
# This script calculates the maximum car price you can afford based on your financial parameters.
#
# Example commands:
#    - Basic calculation with default parameters:
#      python car_price_calculator.py
#
#    - Custom financial parameters:
#      python car_price_calculator.py --max_monthly 800 --down_payment 15000 --trade_in 5000 --min_rate 4.5 --max_rate 6.0
#
#    - Different loan term (in months):
#      python car_price_calculator.py --loan_term 72
