import scipy.stats

def spearmanRho(file1="Wildebeest_data.csv", file2="Lion_data.csv"):
    '''
    -Runs Spearman correlation test to see if two animal populations are related
    -for two files containing data with header on first line, animal data
     separated by commas on rest of lines
    -year is second value in each line, population is third value in each line
    -It also checks to make sure that the years match
     up as some data sets may skip years'''
    
    #opens first file and creates list with year and
    #population data in list of lists
    f1 = open(file1, 'r')
    next(f1) #starts reading at 2nd line, ignoring header row
    data1 = []
    for line in f1:
        line = line.split(",")
        line[2] = line[2].strip('\n')
        data1.append(line[1:])
    
    #opens second file and creates list with year and population data as in list of lists
    f2 = open(file2, 'r')
    next(f2) #starts reading at 2nd line, ignoring header row
    data2 = []
    for line in f2:
        line = line.split(",")
        line[2] = line[2].strip('\n')
        data2.append(line[1:])
    
    #initializes two lists to collect data for years that match up
    datas_1 = []
    datas_2 = []
            
    #compares each year in second list with all the years in the first list
    #appends the population data to appropriate list for years that
    #match up
    for item in data2:
        for thing in data1:
            if item[0]==thing[0]:
                datas_2.append(item[1])
                datas_1.append(thing[1])
   
    #converts all data values to int
    datas_1 = map(int, datas_1)
    datas_2 = map(int, datas_2)
    
    #runs spearman test
    return scipy.stats.spearmanr(datas_1, datas_2)
    
print spearmanRho()