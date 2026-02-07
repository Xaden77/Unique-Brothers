import os
from datetime import datetime,timedelta 
class Logic:
    def __init__(self,Store):
        self.Store=Store
        self.online=[["Online Purchase","Amount"]]
        self.data2=[["Online Purchase","Amount","Cash Purchase","Amount"]]
    def store(self,date,cash,upi,source,amount,hand,credit,purchase):
        if not cash.isdigit() or not upi.isdigit() or not hand.isdigit() or not credit.isdigit():
            return 1
        if not amount=="" and not source=="":
            if purchase=="Online Expense":
                temp=[source,amount,"",""]
                self.data2.append(temp)
                temp = temp[:-2]
                self.online.append(temp) 
            if purchase=="Cash Expense":
                temp=["","",source,amount]
                self.data2.append(temp)
        elif amount=="" and source=="":
            if len(self.data2)<=1:
                return 1
        else:
            return 1
        self.data2 = [data for data in self.data2 if data[2] != ""]
        while len(self.data2)<len(self.online):
            self.data2.append(["","","",""])
        for a,b in zip(self.online,self.data2):
            b[0]=a[0]
            b[1]=a[1]
        self.online=[["Online Purchase","Amount"]]
        folder=r"C:\ub"
        os.makedirs(folder, exist_ok=True)
        self.date=date.replace("/","_")
        if os.path.exists(f"c:\\ub\\{self.date}.docx"):
            return 2
        
    def store2(self,date):
        date_obj = datetime.strptime(date, "%d/%m/%Y")
        prev = date_obj - timedelta(days=1)
        prevDate=prev.strftime("%d/%m/%Y")
        self.prevDate=prevDate.replace("/","_")
        if not os.path.exists(f"c:\\ub\\{self.prevDate}.docx"):
            return 3
        
    def store3(self,cash,upi,credit,hand):
        self.Store.docc(self.date)
        
        self.Store.opening_balance(self.prevDate)
        
        profit=int(cash)+int(upi)+int(credit)
        self.Store.sales(cash,upi,credit,profit)
        
        onlineloss=0
        cashloss=0
        for i in range(1,len(self.data2)):
            if self.data2[i][1]!='':
                onlineloss=onlineloss+int(self.data2[i][1])
            if self.data2[i][3]!='':
                cashloss=cashloss+int(self.data2[i][3])
        loss=onlineloss+cashloss
        self.Store.expense(self.data2,onlineloss,cashloss,loss)
        
        dayTotal = profit-loss
        account = dayTotal-int(hand)
        self.Store.net_sales(str(account),hand,dayTotal)
        self.Store.info(self.date)                                            
        self.Store.save(self.date)
        if os.path.exists(f"c:\\ub\\{self.date}.docx"):
            return 1
        else:
            return 0
    def cont(self,source,amount,purchase):
        if (source=="" or not amount.isdigit()):
            return 1
        if purchase=="Online Expense":
            temp=[source,amount,"",""]
            self.data2.append(temp)
            temp = temp[:-2]
            self.online.append(temp)
        if purchase=="Cash Expense":
            temp=["","",source,amount]
            self.data2.append(temp)  
        
    def rem(self):
        if len(self.data2)<=1:
            return 1
        self.data2.pop()
        
    def kill(self):
        self.data2=[["Online Purchase","Amount","Cash Purchase","Amount"]]
        self.online=[["Online Purchase","Amount"]]
        
    def switch(self):
       pass

    def view(self):
        contents=""
        row=""
        for data in self.data2:
            for i,j in enumerate(data):
                if i == 0 or i==2:
                    row=row+f"{j:<30}"
                elif i ==1 or i==3:
                    row=row+f"{j:<10}"
            contents=contents+row+"\n"
            row=""
        temp=contents
        contents=""

        return temp
