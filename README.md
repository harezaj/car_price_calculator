# Car Affordability Calculator

A Python tool that helps you calculate the maximum car price you can afford based on your financial parameters.

## Features

- Calculate maximum affordable car price based on:
  - Monthly payment budget
  - Down payment amount
  - Trade-in value
  - Interest rates
  - Loan term
- Display multiple affordability options with different combinations of:
  - Down payment amounts
  - Interest rates
  - Loan amounts
- Provide detailed breakdown of the best option

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/car-affordability-calculator.git
   cd car-affordability-calculator
   ```

2. Install required packages:
   ```
   pip install pandas numpy
   ```

## Usage

### Basic Usage

```bash
python car_price_calculator.py
```

This will calculate your maximum affordable car price based on default financial parameters:
- Monthly payment: $750
- Loan term: 60 months
- Down payment: $20,000
- Trade-in value: $6,000
- Interest rate range: 5.0% - 6.0%

### Customizing Financial Parameters

```bash
python car_price_calculator.py --max_monthly 800 --down_payment 15000 --trade_in 5000 --min_rate 4.5 --max_rate 6.0
```

### Different Loan Term

```bash
python car_price_calculator.py --loan_term 72
```

## How It Works

The calculator uses the following approach:
1. Considers various combinations of down payments and interest rates
2. For each combination, calculates the maximum loan amount that stays within your monthly payment budget
3. Adds the loan amount, down payment, and trade-in value to determine the total affordable car price
4. Sorts the results to show the highest affordable car price options

## Example Output

```
Top 10 Affordable Car Price Options:
     Max Car Price  Money Down  Interest Rate (%)  Loan Amount  Monthly Payment
206          65500       20000                5.0        39500       745.413729
136          65000       20000                5.5        39000       744.945325
205          65000       20000                5.0        39000       735.978112
204          64500       20000                5.0        38500       726.542495
67           64500       20000                6.0        38500       744.312859
...

Maximum affordable car price: $65,500

Financial Parameters Summary:
Monthly Payment Budget: $750
Loan Term: 60 months
Down Payment: $20,000
Trade-in Value: $6,000
Interest Rate Range: 5.0% - 6.0%

Best Option Details:
Maximum Car Price: $65,500
Down Payment: $20,000
Trade-in Value: $6,000
Loan Amount: $39,500
Interest Rate: 5.0%
Monthly Payment: $745.41
```

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 