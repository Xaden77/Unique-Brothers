import os
from datetime import datetime, timedelta


class Logic:
    def __init__(self, Store):
        self.Store = Store
        self.data2 = [["Online Purchase", "Amount", "Cash Purchase", "Amount"]]

    def _rebuild(self):
        """Re-merge online and cash entries side-by-side into data2."""
        online_rows = [r for r in self.data2[1:] if r[0] != ""]
        cash_rows   = [r for r in self.data2[1:] if r[2] != ""]
        max_len = max(len(online_rows), len(cash_rows), 0)
        merged = []
        for i in range(max_len):
            o = online_rows[i] if i < len(online_rows) else ["", "", "", ""]
            c = cash_rows[i]   if i < len(cash_rows)   else ["", "", "", ""]
            merged.append([o[0], o[1], c[2], c[3]])
        self.data2 = [["Online Purchase", "Amount", "Cash Purchase", "Amount"]] + merged

    def store(self, date, cash, upi, source, amount, hand, credit, purchase):
        if not cash.isdigit() or not upi.isdigit() or not hand.isdigit() or not credit.isdigit():
            return 1

        if source != "" and amount != "":
            if purchase == "Online Expense":
                self.data2.append([source, amount, "", ""])
            elif purchase == "Cash Expense":
                self.data2.append(["", "", source, amount])
            self._rebuild()
        elif source == "" and amount == "":
            if len(self.data2) <= 1:
                return 1
        else:
            return 1

        folder = r"C:\ub"
        os.makedirs(folder, exist_ok=True)
        self.date = date.replace("/", "_")
        if os.path.exists(f"c:\\ub\\{self.date}.docx"):
            return 2
        return 0

    def store2(self, date):
        date_obj = datetime.strptime(date, "%d/%m/%Y")
        prev = date_obj - timedelta(days=1)
        self.prevDate = prev.strftime("%d_%m_%Y")
        if not os.path.exists(f"c:\\ub\\{self.prevDate}.docx"):
            return 3

    def store3(self, cash, upi, credit, hand):
        self.Store.docc(self.date)
        self.Store.opening_balance(self.prevDate)

        profit = int(cash) + int(upi) + int(credit)
        self.Store.sales(cash, upi, credit, profit)

        onlineloss = sum(int(r[1]) for r in self.data2[1:] if r[1] != "")
        cashloss   = sum(int(r[3]) for r in self.data2[1:] if r[3] != "")
        loss = onlineloss + cashloss

        self.Store.expense(list(self.data2), onlineloss, cashloss, loss)

        net_day = profit - loss
        account = net_day - int(hand)
        self.Store.net_sales(str(account), hand, net_day)

        try:
            self.Store.info(self.date, net_day)
            self.Store.save(self.date)
        except Exception as e:
            import traceback
            traceback.print_exc()   # full details visible in terminal for debugging
            return 3   # file locked or other IO error — gui will warn user to close Word

        if os.path.exists(f"c:\\ub\\{self.date}.docx"):
            return 1
        return 0

    def cont(self, source, amount, purchase):
        if source == "" or not amount.isdigit():
            return 1
        if purchase == "Online Expense":
            self.data2.append([source, amount, "", ""])
        elif purchase == "Cash Expense":
            self.data2.append(["", "", source, amount])
        self._rebuild()   # re-merge immediately so view() is always correct

    def rem(self):
        if len(self.data2) <= 1:
            return 1
        # Find and remove the last entry of whichever type was added last
        # Work backwards through merged rows to find the last non-empty cell
        for i in range(len(self.data2) - 1, 0, -1):
            row = self.data2[i]
            if row[0] != "" or row[2] != "":
                # Clear whichever side was filled last
                # We track this by checking which side has the "later" entry —
                # since entries are added sequentially, pop the last raw entry instead
                break
        # Simpler: pop last raw entry from a shadow list approach —
        # instead, just find the last row with any content and blank the
        # side that was most recently added (we can't know without a log,
        # so blank the LAST non-empty side scanning right-to-left)
        for i in range(len(self.data2) - 1, 0, -1):
            row = self.data2[i]
            if row[2] != "":          # cash side — remove it
                row[2] = ""
                row[3] = ""
                break
            elif row[0] != "":        # online side — remove it
                row[0] = ""
                row[1] = ""
                break
        # Drop any rows that are now completely empty
        self.data2 = [self.data2[0]] + [r for r in self.data2[1:] if r[0] != "" or r[2] != ""]
        self._rebuild()

    def kill(self):
        self.data2 = [["Online Purchase", "Amount", "Cash Purchase", "Amount"]]

    def switch(self):
        pass  # Toggle is handled entirely in gui.py

    def view(self):
        W_NAME = 28
        W_AMT  = 8
        contents = ""
        for data in self.data2:
            online_name, online_amt, cash_name, cash_amt = data
            # Always use fixed widths so cash column never drifts left/right
            contents += (
                f"{online_name:<{W_NAME}}{online_amt:<{W_AMT}}"
                f"{cash_name:<{W_NAME}}{cash_amt:<{W_AMT}}\n"
            )
        return contents