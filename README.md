# TDAmeritrade-Python-API


(AUTHENTICATION)

AUTH.PY
1. Run “python3 auth.py” with admin privs
2. Point servers web browser to link given in program stdout ( Change “HARTLEYCAP1” with your App specific code )
3. enter TD credentials and accept browser redirect warning
4. If it worked, you should see a page that showes access/ refresh token. You can CTRL-C after it says “wrote tokens to file” and your now authorized for the API

REFRESH.PY
1. Run with admin privs
2. Gets new auth token every 30 mins before they expire in a loop


(ORDERS)

CANCELORDER.PY
- Just run “python3 cancelOrder.py <ORDER_ID#>

GETORDER.PY
- Python3 getOrder.py <ORDER_ID#>

GETORDERS.PY
- Python3 getOrders.py
- Dumps all working orders to .csv file

PLACEORDER.PY
- Python3 placeOrder.py <ORDER.CSV>
- ORDER.CSV is same syntax as output from getOrders.py output
- You can edit the row[] settings in the .py file if you want to use a different order.csv format

REPLACEORDER.py
- Takes Two arguments.
- Argument 1 is OrderID
- Argument 2 is Order CSV file containing order params
- Eg: python3 replaceOrder.py <ORDER_ID> <ORDER.CSV>


( ACCOUNTS )

GETACCOUNT.PY
- Takes no arguments
- Outputs two csv files. One holds account balances and the other has position information.

GETACCOUNTS.PY
- Didn’t do this one since I only have one account to work with and I’m assuming your situation is the same. If you really do need this one let me know and I’ll make it happen.


( TRANSACTIONS ) 

GETTRANSACTION.PY
- Takes one Argument ( Order ID )

GETTRANSACTIONS.PY
- Takes no Arguments 
