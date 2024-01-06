#This function is the heart of this program!
def loadCSVData(fileName):      #This functions will use the csv files (excel files either TopUni or capitals) and make it tangeble  that we can later use!
    listInfoSorted = []     #This list will contain lists that include each line in fileName orginazed and ready to use when the function is called!
    try:
        fileContent = open(fileName, "r", encoding='utf8')  # Here we will open the fileName and read it as csv (denoted by the utf8).
        next(fileContent)   # Skipping the first header of the fileName since there is no use of it!
        for line in fileContent:
            OrgnaizedLine = (line.strip("\n").split(","))   # Here we will orginaze each line in fileName by using strip and split functions!
            listInfoSorted.append(OrgnaizedLine)    # Will store it in our listInfoStored
        fileContent.close()
    except FileNotFoundError:     # We use FileNotFoundError in case the file name that was provided is not regcognized in our program! In this case the file names must be TopUni.csv and capitals.csv.
        print("file not found")
        quit()
    return listInfoSorted

def numOfUni(topUni):      # This function will count the number of universites available in TopUni.csv file!
    loadCSVData(topUni)
    uniRanks = []   # This will store university ranks which can be used to detect the number of universities available!
    for info in loadCSVData(topUni):
        uniRanks.append(info[0])
    numberUni = len(uniRanks)   # This will detect the number of universities!
    return numberUni

def namesOfCount(topUni):   # This function will find names of the available countries that have universities in TopUni.csv!
    aviblCount = []     # The available countries will be stored here.
    for info in loadCSVData(topUni):
        if info[2].upper() not in aviblCount:   # This condition will only append coutries that are not already in the list.
            aviblCount.append(info[2].upper())
    return aviblCount

def availableContinents(topUni, capitals):  # This function will find the continent names available in the capitals.csv!
    continents = []     # will store the continent names!
    for countries in namesOfCount(topUni):
        for info in loadCSVData(capitals):
            if countries == info[0].upper():
                if info[5].upper() not in continents:   # This condition will only append continents that are not in the list.
                    continents.append(info[5].upper())
    myString = ', '.join(map(str, continents))  # Here we convert the list into a string!
    return myString

def topInternatRank(selectedCountry, topUni):   # This function will find the highest international rank with the university name available in the selected country!
    uniWithTopInterRank = []     # Here it will store the highest international rank with its uni name in the selected country!
    uniRankCount = []   # Here it will store the sorted international ranks of all universities within the selected country!
    for info in loadCSVData(topUni):
        if selectedCountry.upper() in info[2].upper():
            uniRankCount.append(int(info[0]))
    uniRankCount.sort()     # Sorting the uniRankCount form lowest international rank to the highest!
    for info in loadCSVData(topUni):
        if str(uniRankCount[0]) == info[0]:     # This condition will provide the higest international score and its corresponding uni name!
            uniWithTopInterRank.append(info[0])
            uniWithTopInterRank.append(info[1].upper())
    return uniWithTopInterRank

def topNationalRank(selectedCountry, topUni):   # This function will find the highest national rank with the uni name in the selceted country!
    topNatRankWithUniName = []      # This will store the top national rank and its uni name!
    for info in loadCSVData(topUni):
        if selectedCountry.upper() in info[2].upper():
            if info[3] == "1": # This condition will indicate the highest national rank within the selected country!
                topNatRankWithUniName.append(info[3])
                topNatRankWithUniName.append(info[1].upper())
    return topNatRankWithUniName

def theAvgScore(selectedCountry, topUni):   # This function will find avg score of all universities within the selected country!
    scores = []     # This will store all scores within the selected country!
    for info in loadCSVData(topUni):
        if selectedCountry.upper() == info[2].upper():
            scores.append(float(info[8]))   # Appending all scores of the uni in the selected country!
    avgScore = format((sum(scores))/(len(scores)), '.2f')   # This will calculate the avg score to two decimal places!
    return avgScore

def contRelScore(selectedCountry, topUni, capitals): # This function will calculate the relative score!
    countCorrespondCont = []    # This list will store all countries and continents in capitals.csv.
    countCorrespondContSorted = []      # This list will store lists where each list will contain a country and its corresponding continents.
    countAndContWithUni = []    # This list will contain lists in which each list indicates the country (with its corresponding continents) that at least has one university in TopUni.csv.
    contScore = []      # This list will store the scores of all universities within the chosen continent sorted from lowest to highest!
    contWithScoreAndRelScore = []   # This list will contain the continent, highest score within that continents, and the calculated relative score!
    for info in loadCSVData(capitals):
        countCorrespondCont.append(info[0])
        countCorrespondCont.append(info[5])
    for info in range(0, len(countCorrespondCont), 2):      # This loop will sort the countCorrespondCont and append it to new list!
        countCorrespondContSorted.append(countCorrespondCont[info:info + 2])
    for rows in countCorrespondContSorted:
        for info in loadCSVData(topUni):
            if info[2].upper() == rows[0].upper():
                rows.append(float(info[8]))      # Here we will append the scores of all university with the same country in each of the list in countCorrespondContSorted!
    for rows in countCorrespondContSorted:
        if len(rows) > 2: # This condition is created to sort out countries with and without universities in TopUni.csv!
            countAndContWithUni.append(rows)     # The relevant lists will be appended to countAndContWithUni  for organization purposes
    continent = ""
    for rows in countAndContWithUni:
        if selectedCountry.upper() == rows[0].upper():
            continent = rows[1].upper()     # This will indicate the continent of the selected country!
            contWithScoreAndRelScore.append(continent) # And it will store it in contWithScoreAndRelScore!
        if continent in rows[1].upper():    # This condition will check the continent indicated by the selectedCountry in each element of countAndContWithUni!
            contScore.append(rows[2])    # When matched it will append the highest scores of all universities from that continent!
    contScore.sort()    # Will sort all scores from low to high!
    contWithScoreAndRelScore.append(contScore[-1])      # Will call the highest score from chosen continent and store it in contWithScoreAndRelScore!
    relScore = format(float(theAvgScore(selectedCountry, topUni)) / float(contWithScoreAndRelScore[1]) * 100, '.2f')    # Calculating the relative score!
    contWithScoreAndRelScore.append(relScore)   # Storing the relative score in contWithScoreAndRelScore!
    return contWithScoreAndRelScore

def capitalCity(selectedCountry, capitals):     # This function will find the capital of the selected country!
    for info in loadCSVData(capitals):
        if selectedCountry.upper() == info[0].upper():  # This condition will indicate if the selected country matches the counrty in capitals.csv!
            capitalOfCountry = info[1].upper()  # If matched it will indicate the capital of that country!
    return capitalOfCountry

def uniWithCapNames(selectedCountry, topUni, capitals):
    uniWithCapNames = []    # This list will store all uni that have the capital city in their name!
    capital = capitalCity(selectedCountry, capitals)
    for info in loadCSVData(topUni):
        if capital.upper() in info[1].upper():      # This condition will check if the capital of the selected country is in the names of all uni in that country!
            uniWithCapNames.append(info[1].upper())
    count = 0
    numberOfUniWithCaps = []    # This list will contain the number of uni that have the capital city in their name!
    for i in range(0, len(uniWithCapNames)):
        count = count + 1       # Calculates the number of uni that have the capital city in their name!
        numberOfUniWithCaps.append(count)
    wholeInfo = []      # This list will contain the numbers with corresponding university!
    for info in uniWithCapNames:
        wholeInfo.append("#" + str(numberOfUniWithCaps[0]) + " " + info)
        numberOfUniWithCaps.pop(0)
    string = ' \n'.join(str(x) for x in wholeInfo) # Will convert the wholeInfo list into string in the correct format!
    return string

def getInformation(selectedCountry, topUni, capitals): # This function will provide all of necessary outpouts indicated by the user! Note that this function will call other functions to display the necessary infomation!
    file = open("output.txt", "w")
    file.write(f"Total number of universities => {numOfUni(topUni)}\n")
    file.write(f"Available countries => {', '.join(map(str, namesOfCount(topUni)))}\n")
    file.write(f"Available continents => {availableContinents(topUni, capitals)}\n")
    file.write(f"followsAt international rank => {topInternatRank(selectedCountry, topUni)[0]} the university name is => {topInternatRank(selectedCountry, topUni)[1]}\n")
    file.write(f"At national rank => {topNationalRank(selectedCountry, topUni)[0]} the university name is => {topNationalRank(selectedCountry, topUni)[1]}\n")
    file.write(f"The average score => {theAvgScore(selectedCountry, topUni)}%\n")
    file.write(f"The relative score to the top university in {contRelScore(selectedCountry,topUni ,capitals)[0]} is => ({theAvgScore(selectedCountry, topUni)} / {contRelScore(selectedCountry,topUni ,capitals)[1]}) x 100% = {contRelScore(selectedCountry,topUni ,capitals)[2]}%\n")
    file.write(f"The capital is => {capitalCity(selectedCountry, capitals)}\n")
    file.write(f"The universities that contain the capital name => \n{uniWithCapNames(selectedCountry, topUni, capitals)}\n")
    file.close() # Will close and save the txt file!
    return file
