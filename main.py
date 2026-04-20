from gui import Win1
from logic import Logic
from store import Store

store = Store()
logic = Logic(store)
gui = Win1(logic)
gui.mainloop()