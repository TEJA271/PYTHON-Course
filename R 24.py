# 24.Format datetime output

from datetime import datetime

now = datetime.now()


formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted datetime:", formatted)

