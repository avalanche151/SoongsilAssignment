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
                table.write(','.join(i) + "\n")
            else:
                table.write(','.join(i))
        table.close()

    def addRec(self,dict):
        self.rec=dict
        table=open(f"{self.tblName}.TBL","a")
        table.write("\n")
        table.write(",".join(list(self.rec.values())))
        table.close()
        
    def searchAllRec(self):
        self.recGroup=[]
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
                return searchkey
                
        else:
            return False
    def searchAllbyKey(self,searchvalue,searchby):
        searchlist=[]
        for i in range(len(self.recGroup)):    
            if searchvalue in self.recGroup[i][searchby]:    
                searchlist.append(self.recGroup[i])
        return searchlist

    def removeRec(self,delvalue,delby):
        for i in range(len(self.recGroup)):
            if delvalue == self.recGroup[i][delby]:
                del(self.recGroup[i])
                return True
        else:
            return False
    

    def modifyRec(self,modifyvalue,modifyby,li):
        for i in range(len(self.recGroup)):
            if modifyvalue==self.recGroup[i][modifyby]:
                self.recGroup[i]=li
                return True
        else:
            return False


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
        if os.path.exists(f"{tblName}.TBL")==False:
            tbl.createTBL()
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
tbl=TBL(tblname,tblattribute)
while True:
    b=int(input("\n작업을 선택하세요.\n1. 고객 정보 입력\n2. 고객 아이디로 정보 수정\n3. 고객 아이디로 정보 삭제\n4. 고객 아이디로 정보 조회\n5. 고객명으로 정보 조회\n6. 특정 지역명으로 아이디 조회\n0. 종료\n"))
    if b==1:
        cInfo={"id":"","name":"","job":"","addr":"","cp":"","point":""}
        print("\n고객 정보를 입력합니다.")
        cInfo['id']=input("고객 아이디: ")
        cInfo['name']=input("이름: ")
        cInfo['job']=input("직업: ")
        cInfo['addr']=input("주소: ")
        cInfo['cp']=input("전화번호: ")
        cInfo['point']=input("포인트: ")
        tbl.addRec(cInfo)
        print("\n고객 정보가 입력되었습니다.\n")
    elif b==2:
        findbyID=input("\n수정할 고객님의 아이디를 입력하세요: ")
        tbl.searchAllRec()
        cInfo={"id":"","name":"","job":"","addr":"","cp":"","point":""}
        print("고객 정보를 수정합니다")
        cInfo['id']=input("고객 아이디: ")
        cInfo['name']=input("이름: ")
        cInfo['job']=input("직업: ")
        cInfo['addr']=input("주소: ")
        cInfo['cp']=input("전화번호: ")
        cInfo['point']=input("포인트: ")
        isModified=tbl.modifyRec(findbyID,0,list(cInfo.values()))
        if isModified==True:
            tbl.rewriteTBL()
            print(f"\n{findbyID} 고객님의 정보가 수정되었습니다.")
        else:
            print(f"\n{findbyID} 고객님의 정보는 존재하지 않습니다.")
    
    elif b==3:
        findbyID=input("\n삭제할 고객님의 아이디를 입력하세요: ")
        tbl.searchAllRec()
        isRemoved=tbl.removeRec(findbyID,0)
        if isRemoved==True:
            tbl.rewriteTBL()
            print(f"\n{findbyID} 고객님의 정보가 삭제되었습니다.")
        else:
            print(f"\n{findbyID} 고객님의 정보는 존재하지 않습니다.")
        

    elif b==4:
        findbyID=input("\n조회할 고객님의 아이디를 입력하세요:")
        tbl.searchAllRec()
        customerinfo=tbl.searchRec(findbyID,0)
        if customerinfo==False:
            print(f"\n{findbyID} 고객님의 정보는 존재하지 않습니다.")
        else:
            print(f"\n{findbyID}님의 정보는 다음과 같습니다.")
            print(f"\n고객 아이디: {customerinfo[0]}\n이름: {customerinfo[1]}\n직업: {customerinfo[2]}\n주소: {customerinfo[3]}\n전화번호: {customerinfo[4]}\n포인트: {customerinfo[5]}")
             
        

    elif b==5:
        findbyName=input("\n조회할 고객님의 이름을 입력하세요:")
        tbl.searchAllRec()
        customerinfo=tbl.searchRec(findbyName,1)
        if customerinfo==False:
            print(f"\n{findbyName} 고객님의 정보는 존재하지 않습니다.")
        else:
            print(f"\n{findbyName}님의 정보는 다음과 같습니다.")
            print(f"\n고객 아이디: {customerinfo[0]}\n이름: {customerinfo[1]}\n직업: {customerinfo[2]}\n주소: {customerinfo[3]}\n전화번호: {customerinfo[4]}\n포인트: {customerinfo[5]}")

    elif b==6:
        findbyGeo=input("\n조회할 지역명을 입력하세요.")
        tbl.searchAllRec()
        customerinfolist=tbl.searchAllbyKey(findbyGeo,3)
        if customerinfolist==[]:
            print("\n지역에 고객이 존재하지 않습니다.")
        else:
            print(f"\n{findbyGeo} 지역 고객님들의 아이디 목록입니다.")
            for i in range(len(customerinfolist)):
                print(customerinfolist[i][0],end=",")

                
    elif b==0:
        print("프로그램을 종료합니다.")
        break



