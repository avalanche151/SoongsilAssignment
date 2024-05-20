import os

class TBL:
    
    def __init__(self,tblName,attList):
        self.tblName=tblName
        self.attList=attList
        self.rec={}
        self.recGroup=[]

    def createTBL(self):
        table=open(f"{self.tblName}.TBL","w")
        table.write(",".join(self.attList))
        table.close

    def deleteTBL(self):
        os.remove(f"{self.tblName}.TBL")

    def addRec(self):
        table=open(f"{self.tblName}.TBL","a")
        table.write(",".join(list(self.rec.values())))
        
    
    def removeRec(self):
        table=open(f"{self.tblName}.tbl","w")
        table
        
class DB:
    
    def __init__(self,dbName):
        self.dbName=dbName
        self.tblList=[]
    def createDB(self):
        database=open(f"{self.dbName}.db","w")
        database.close()

    def deleteDB(self):
        os.remove(f"{self.dbName}.db")

    def createTBL(self,tblName,attList):
        tbl = TBL(tblName,attList)
        tbl.creatTBL()
        self.tblList.append(tblName)
    
    def deleteTBL(self,tblName,attList):
        tbl = TBL(tblName,attList)
        tbl.deleteTBL()
        self.tblList.remove(tblName)
    
        
        
        


