# CodeAlpha Internship – Task 2: Stock Portfolio Tracker

### Project Overview
This is a simple *Stock Portfolio Tracker* built using Python.  
It calculates your total investment value based on predefined stock prices and user-input quantities.

###Features
- Predefined stock price dictionary (e.g., AAPL, TSLA, GOOG)
- User inputs stock symbols and quantities  
- Calculates and displays total investment value  
- Option to save the summary in a .txt file  

###Concepts Used
dictionary, input/output, basic arithmetic, file handling

###How to Run
1. Make sure Python is installed on your system.  
2. Download the file CodeAlpha_stock_portfolio.py.  
3. Run the file.

###Example output
Welcome to Stock Portfolio Tracker!
Available stocks and their prices (USD):
AAPL: $180
TSLA: $250
GOOG: $120
MSFT: $300
AMZN: $140

Enter your stocks. Type 'done' to finish.

Enter stock symbol (e.g., AAPL): AAPL
Enter quantity of AAPL: 5
 Added 5 of AAPL worth $900

Enter stock symbol (e.g., AAPL): TSLA
Enter quantity of TSLA: 2
 Added 2 of TSLA worth $500

Enter stock symbol (e.g., AAPL): GOOG
Enter quantity of GOOG: 4
Added 4 of GOOG worth $480

Enter stock symbol (e.g., AAPL): done

===== Portfolio Summary =====
AAPL - 5 shares × $180 = $900
TSLA - 2 shares × $250 = $500
GOOG - 4 shares × $120 = $480
==============================
 Total Investment: $1880
==============================

Do you want to save the result to a file? (y/n): y
 Results saved to 'portfolio_summary.txt'.

 Thank you for using the Stock Portfolio Tracker!
