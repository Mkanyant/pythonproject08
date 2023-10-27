# OOP

class IoTSAU :
    #data/property/field/attyibute
    major = "SAU"
    name = ""

    #matod (มันคือฟังก์ชัน แต่เราเราไม่เรียกฟังก์ชัน)
    def showHi(salf) :
        print('Hi........')

    def infroduceMyself(self) :
        print(f'My name is {self.major}')
        print(f'My major is {self.major}')

#--------------------
#สร้าง object
obA = IoTSAU() #
obB = IoTSAU()

#
print( obA.major)
obA.major = "wow"
obA.name = "ฟ้าร้อง"
obB.name = "ฝนตกแล้ว"