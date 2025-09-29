from docx import Document

class Store():
    def __init__(self):
        pass
    def docc(self,date):
        self.doc=Document()
        self.data=[]
        self.data1=[]
        self.doc.add_heading(f"Sales and Expenditure report on {date}",level=0)

    def opening_balance(self,date):
        try:
            doc1=Document(f"c:\\ub\\{date}.docx")
            table=doc1.tables[3]
            for i, row in enumerate(table.rows):
                row_data = []
                for j, cell in enumerate(row.cells):
                    row_data.append(cell.text.strip())
                self.data.append(row_data)
            strPrevDayTotal=self.data[3][1]
            self.prevDayTotal=strPrevDayTotal.partition("=")[2]
            table0=self.doc.add_table(rows=1,cols=2)
            table0.style="Table Grid"
            table0.cell(0,0).text = "Opening Balance"
            table0.cell(0,1).text = self.prevDayTotal
        except Exception as e:
            print(e)
            table0=self.doc.add_table(rows=1,cols=2)
            table0.style="Table Grid"
            table0.cell(0,0).text = "Opening Balance"
            self.prevDayTotal="0"
            table0.cell(0,1).text = self.prevDayTotal
            
    def sales(self,cash,upi,credit,profit):
        self.profit=profit
        self.doc.add_heading("Sales",level=1)
        self.data1 = [   ["Cash Sales", cash],
                    ["Phone Pay Sales", upi],
                    ["Credit sales", credit],
                    [" ", " "],
                    ["Total Sales", self.profit]  ]
        table1 = self.doc.add_table(rows=len(self.data1), cols=len(self.data1[0]))
        table1.style = "Table Grid"
        for i, row in enumerate(self.data1):
            for j, cell in enumerate(row):
                table1.cell(i, j).text = str(cell)
                
    def expense(self,data2,onlineLoss,cashLoss,loss):
        self.loss=loss
        self.doc.add_heading("Purchase and Expense",level=1)
        data2.append(["","","",""])
        data2.append(["Online Expenses",onlineLoss,"Cash Expenses",cashLoss])
        data2.append(["","","",""])
        data2.append(["Total Expense","","",self.loss])
        table2 = self.doc.add_table(rows=len(data2), cols=len(data2[0]))
        table2.style = "Table Grid"
        for i, row in enumerate(data2):
            for j, cell in enumerate(row):
                table2.cell(i, j).text = str(cell)
       
    def net_sales(self,account,hand,total):
        self.doc.add_heading("Net Balance",level=1)
        table3 = self.doc.add_table(rows=4,cols=2)
        strDayTotal = str(f"{self.profit} - {self.loss} = {total}")  
        grandTotal=int(self.prevDayTotal) + total
        strGrandTotal=str(f"{total} + {self.prevDayTotal} = {grandTotal}")
        table3.style="Table Grid"
        table3.cell(0,0).text = "Per day Balance"
        table3.cell(0,1).text = strDayTotal
        table3.cell(1,0).text = "Cash in Hand"
        table3.cell(1,1).text = hand
        table3.cell(2,0).text = "Cash at Bank"
        table3.cell(2,1).text = account
        table3.cell(3,0).text = "Closing Balance"
        table3.cell(3,1).text = strGrandTotal
    def save(self,date):
        self.doc.save(f"c:\\ub\\{date}.docx")