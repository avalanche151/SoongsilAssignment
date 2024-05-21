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
        table.close()

    def deleteTBL(self):
        os.remove(f"{self.tblName}.TBL")
    
    def clearTBL(self):
        table=open(f"{self.tblName}.TBL","w")
        table.write("")
        table.close()
    
    def rewriteTBL(self):
        table=open(f"{self.tblName}.tbl","w")
        for num, i in enumerate(self.recGroup):
            if num+1 < len(self.recGroup):
                table.write(', '.join(i) + "\n")
            else:
                table.write(', '.join(i))
        table.close()

    def addRec(self,dict):
        self.rec=dict
        table=open(f"{self.tblName}.TBL","a")
        table.write(",".join(list(self.rec.values())))
        table.close()
        
    def searchAllRec(self):
        table=open(f"{self.tblName}.tbl","r")
        allLines=table.readlines()
        for line in allLines:
            line=line.strip()
            self.recGroup.append(line.split(','))
        table.close()

    def searchRec(self,searchvalue,searchby):
        for i in range(len(self.recGroup)):
            if searchvalue==self.recGroup[i][searchby]:
                searchkey=self.recGroup[i]
                break
        return searchkey

    def removeRec(self,delvalue,delby):
        for i in range(len(self.recGroup)):
            if delvalue==self.recGroup[i][delby]:
                del(self.recGroup[i])
                break
    

    def modifyRec(self,modifyvalue,modifyby,li):
        for i in range(len(self.recGroup)):
            if modifyvalue==self.recGroup[i][modifyby]:
                self.recGroup[i]=li
                break


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
    
        
db=DB("customerDB")
db.createDB()
tblname="customerTBL"
tblattribute=['ID','NAME','JOB','ADDR','CP','POINT']
db.createTBL(tblname,tblattribute)

while True:
    b=int(input("\n작업을 선택하세요.\n1. 고객 정보 입력\n2. 고객 아이디로 정보 수정\n3. 고객 아이디로 정보 삭제\n4. 고객 아이디로 정보 조회\n5. 고객명으로 정보 조회\n6. 특정 지역명으로 정보 조회\n0. 종료\n"))
    if b==1:
        cInfo={"id":"","name":"","addr":"","job":"","CP":"","point":""}
        print("\n고객 정보를 입력합니다.")
        cInfo['id']=input("고객 아이디: ")
        cInfo['name']=input("이름: ")
        cInfo['addr']=input("주소: ")
        cInfo['job']=input("직업: ")
        cInfo['cp']=input("전화번호: ")
        cInfo['point']=input("포인트: ")
        tbl=TBL(tblname,tblattribute)
        tbl.addRec(cInfo)
        print("\n고객 정보가 입력되었습니다.\n")
    elif b==2:
         findbyName=input("\n수정할 고객님의 아이디를 입력하세요: ")
         if cInfo["name"]==findbyName:
             print(f"\n{findbyName} 고객님의 고객 정보는 다음과 같습니다.")
             print(f"\n고객 아이디: {cInfo['id']}\n이름: {cInfo['name']}\n주소: {cInfo['addr']}\n직업: {cInfo['job']}\n전화번호: {cInfo['CP']}\n")
         else:
             print(f"{findbyName} 고객님의 정보는 존재하지 않습니다.")
    elif b==3:
         findbyID=input("\n조회할 고객 아이디를 입력하세요: ")
         if cInfo["id"]==findbyID:
             print(f"\n고객 아이디 {findbyID}의 정보는 다음과 같습니다.")
             print(f"\n고객 아이디: {cInfo['id']}\n이름: {cInfo['name']}\n주소: {cInfo['addr']}\n직업: {cInfo['job']}\n전화번호: {cInfo['CP']}\n")
         else:
             print(f"{findbyID} 고객님의 정보는 존재하지 않습니다.")
    elif b==0:
        print("프로그램을 종료합니다.")
        break



