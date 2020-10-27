arrRange = 0


def main():
    print("Uygun yolu bulmak içim her seferinde bir artacak şekilde sayi dizisini girin."
          "\nHer bir rakam dizsini girerken rakamlarin aralarinda bir bosluk bırakin."
          "\nÖrn: "
          "\n1. Dizi:1"
          "\n2. Dizi:11 3"
          "\n3. Dizi:4 54 12"
          "\n4. Dizi:1 5 13 16\n")

    print("Kaç tane dizi istiyorsaniz sayisini girin. Örn: 4\n")
    inpt = input("Dizi sayisi: ")

    if not inpt.isnumeric():
        print("Hatali giris\n")
        main()

    global arrRange
    arrRange = int(inpt)


    istrue = False
    for i in range(arrRange):
        s = input(str(i+1) + ". Dizi:")
        s = s.split()
        istrue = writeToFile(i+1, s)
        if not istrue:
            break

    if istrue:
        findMinPath()


def findMinPath():
    sArr = []
    tArr = []
    fh = open("out.txt", "r")
    for line in fh:
        tArr.append(line.strip())
    #fh.close()

    for i, num in enumerate(tArr):
        sArr.append(num)

    minSum = 0
    pPath = []
    for s in sArr:
        s = s.split()
        minSum = minSum + int(min(s))
        pPath.append(min(s))


    mStr = "Minimum yol: "
    for i, num in enumerate(pPath):
        if i == (len(pPath)-1):
            mStr = mStr + " " + str(pPath[i]) + " = " + str(minSum)
        else:
            mStr = mStr + str(pPath[i]) + " +"
    print(mStr)
    fh.truncate(0)
    fh.close()



def writeToFile(range, val):
    if isEnoughVal(range, val):
        outF = open("out.txt", "a")
        for i in val:
            outF.write(i + " ")
        outF.write("\n")
        outF.close()
        return True

    else:
        print("Hatali giris\n")
        outF = open("out.txt", "a")
        outF.truncate(0)
        outF.close()
        return False


def isEnoughVal(range, val):
    if isNumeric(val):
        if range == len(val):
            return True
        else:
            outF = open("out.txt", "a")
            outF.truncate(0)
            outF.close()
            return False
    else:
        return False


def isNumeric(val):
    for i in val:
        if not (i.isnumeric()):
            outF = open("out.txt", "a")
            outF.truncate(0)
            outF.close()
            return False

    return True


if __name__ == "__main__":
    # execute only if run as a script
    main()