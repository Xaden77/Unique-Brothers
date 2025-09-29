from gui import Win1 as ui
from logic import Logic as lo
from store import Store as st

store=st()
logic=lo(store)
gui=ui(logic)
gui.mainloop()