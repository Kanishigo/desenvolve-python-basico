from datetime import datetime

data = datetime.now()
print (f"Data: {data.strftime('%d/%m/%Y')}")
print (f"Data: {data.strftime('%H:%M')}")