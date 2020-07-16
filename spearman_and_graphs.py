import scipy.stats
import pylab

def spearmanRho(file1="Lion.csv", file2="Blue Wildebeest.csv"):
    '''
    -prints result of Spearman's rank correlation coefficient test to see 
     if two animal populations are related
    -creates two graphs:
        -population of animal 2 vs. population of animal 1
        -side-by-side graphs of animal 1 population vs. year, 
         animal 2 population vs. year
    -uses two csv files containing data with header on first line, animal data
     separated by commas on rest of lines
    -year is second value in each line, population is third value in each line
    -It also checks to make sure that the years match
     up as some data sets may skip years
    '''
    
    #creates variables to store names of each animal from file names
    #for use in graph labels
    animal1 = file1.strip(".csv")
    animal2 = file2.strip(".csv")
    
    data1, years1, pop1 = get_data_from_file(file1)
    data2, years2, pop2 = get_data_from_file(file2)
        
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
   
    #converts all data values to floats
    datas_1 = list(map(float, datas_1))
    datas_2 = list(map(float, datas_2))
    years1 = list(map(float, years1))
    years2 = list(map(float, years2))
    pop1 = list(map(float, pop1))
    pop2 = list(map(float, pop2))
    
    #runs Spearman's rho test
    print (scipy.stats.spearmanr(datas_1, datas_2))
    
    #Creates plot of the population of one animal versus the
    #population of a second animal, formatting the plot appropriately
    fig1, ax = pylab.subplots(1, facecolor = "#FFFAF0")
    pylab.scatter(datas_1, datas_2)
    pylab.title("Population of " + animal2 + " vs. Population of " + animal1)
    pylab.xlabel(file1.strip(".csv") + " Population")
    pylab.ylabel(file2.strip(".csv") + " Population")
    ax.set_facecolor('#D8EFF3')
    
    #Creates side-by-side plot of the two related animals
    fig2, (ax1, ax2) = pylab.subplots(1, 2, facecolor = "#FFFAF0")
    ax1.scatter(years1, pop1)
    ax1.plot(years1, pop1)
    ax2.scatter(years2, pop2, c='r')
    ax2.plot(years2, pop2, c='r')
    ax1.set_title("Population of " + animal1 + " vs. Year")
    ax2.set_title("Population of " + animal2 + " vs. Year")
    ax1.set_xlabel("Year")
    ax2.set_xlabel("Year")
    ax1.set_ylabel(animal1 + " Population")
    ax2.set_ylabel(animal2 + " Population")
    ax1.set_facecolor('#D8EFF3')
    ax2.set_facecolor('#FFE4E1')

    #displays the plots
    pylab.show()

def get_data_from_file(file_name):
    '''
    opens first file and creates list with year and
    population data in list of lists
    also creates year and population data lists for use in graphs
    '''
    f = open(file_name, 'r')
    next(f) #starts reading at 2nd line, ignoring header row
    data = []
    years = []
    pop = []
    for line in f:
        line = line.split(",")
        line[2] = line[2].strip('\n')
        data.append(line[1:])
        years.append(line[1])
        pop.append(line[2])
    return data, years, pop
    
#example function call
spearmanRho("Eurasian kestrel.csv", "Long-eared owl.csv")
