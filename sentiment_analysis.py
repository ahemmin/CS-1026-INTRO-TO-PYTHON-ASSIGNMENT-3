### Average ###
def Average(Tuple):
    Average=0
    if Tuple[0]!=0:     #If Happiness_Score isn't 0, ie.there are tweets with at least one keyword
        Average=round((int(Tuple[0])/int(Tuple[1])),2)   #Tweet Average
    else:
        Average=0

    return Average,Tuple[3],Tuple[2] #Returns tweet average, Number of tweets containing at least 1 keyword, and the regional tweet count

### PROCESSING OF KEYWORDS ###

def Keywords_File_Formatter(Keywords_file):
    New_List=[]
    Text=Keywords_file.readlines() #Reading file by line and inputting into list as seperate elements
    for i in range(0,len(Text)):        #Iterating over list elements
        Text[i]=(Text[i]).rstrip()      #Eliminates \n
        Formatted=(Text[i]).split(",")  #Splits word and corresponding value and inputs into list as elements 0 and 1 respectively
        New_List.append(Formatted)      #Inputs lists into grand list

    return New_List             #Returns grand list (Essentially a table)

### PROCESSING OF TWEETS ###

def String_Processor(Tweet_file,Punctuation_String):
    New_String=""
    for line in Tweet_file:         #Iterates over file by line
        Words1=line.lower()         #Makes lowercase
        for i in range(0,len(Words1)):             #Iterates over line by character
            if Words1[i] not in Punctuation_String:     #Eliminates Punctuation
               New_String=New_String+Words1[i]
               if i > 40:                           #Numbers which require period to be sorted will not go through this part
                   New_String=New_String.rstrip(".")    #Strip periods from string

    return New_String                       #Returns processed string

### CALCULATING SENTINEL SCORE ###

def Happiness_Calculator(Processed_Tweets_Table,Processed_Keywords_Table,Regional_Total_Tweet_Counter):
    Happiness_Score=0
    Number_of_Keywords=0
    Number_of_Tweets_Containing_Keywords=0
    for i in range(0,len(Processed_Tweets_Table)):  #Iterating over table containing tweets are elements (in sublists)
        Variable=False
        for x in range(0,len(Processed_Tweets_Table[i])):   #Iterating over sublist (the tweet which is a list containing words as the elements)
            New_Word=Processed_Tweets_Table[i][x]
            for z in range(0,len(Processed_Keywords_Table)): #Iterating over Keywords table
                if New_Word==(Processed_Keywords_Table[z][0]):
                    Number_of_Keywords=Number_of_Keywords+1
                    Happiness_Score=Happiness_Score+int(Processed_Keywords_Table[z][1])
                    Variable=True
        if Variable==True:      #Adds to Number_of_Tweets_Containing_Keywords only once per tweet
            Number_of_Tweets_Containing_Keywords=Number_of_Tweets_Containing_Keywords+1


    return Happiness_Score,Number_of_Keywords,Regional_Total_Tweet_Counter,Number_of_Tweets_Containing_Keywords

### PRINT RESULTS ###

def Print_Results(Total_Tweets_Counter,Tweets_Table1,Tweets_Table2,Tweets_Table3,Tweets_Table4,List,Tuple1,Tuple2,Tuple3,Tuple4):   #Condensed way of printing info statements when compute_tweets runs
    Total_Tweet_Counter=(len(Tweets_Table1)+len(Tweets_Table2)+len(Tweets_Table3)+len(Tweets_Table4))       #Calculating total tweet count for future use
    print("This file contains "+str(Total_Tweet_Counter)+" tweet(s)")                       #Whole bunch of print statements
    print("The list of tuples for the data from Eastern to Pacific Timezones is: ",List)
    print("Eastern Timezone Data: ",Tuple1)
    print(Conclusion_Writer(Tuple1))
    print("Central Timezone Data: ",Tuple2)
    print(Conclusion_Writer(Tuple2))
    print("Mountain Timezone Data: ",Tuple3)
    print(Conclusion_Writer(Tuple3))
    print("Pacific Timezone Data: ",Tuple4)
    print(Conclusion_Writer(Tuple4))

### Conclusion_Writer ###

def Conclusion_Writer(Tuple):    #Evaluates results and determines conclusion
    Returned1="Regional data set: "+str(Tuple)+".  In total the number of tweets found in the region is "+str(Tuple[2])+", of those tweets "+str(Tuple[1])+" contain(s) at least one keyword from the list. "  #string generalized to all possible results
    if float(Tuple[0])>7.5:
        Returned3=Returned1+"The average sentiment score is "+str(Tuple[0])+", which means the contents of the tweets on average are overall very happy."
        return Returned3   #Returns string containing both the general and value dependent statements
    elif float(Tuple[0])>5.0 and float(Tuple[0])<=7.5:
        Returned4=Returned1+"The average sentiment score is "+str(Tuple[0])+", which means the contents of the tweets on average are overall happy."
        return Returned4    #Returns string containing both the general and value dependent statements
    elif float(Tuple[0])==5.0:
        Returned5=Returned1+"The average sentiment score is "+str(Tuple[0])+", which means the contents of the tweets on average are overall neutral."
        return Returned5    #Returns string containing both the general and value dependent statements
    elif float(Tuple[0])>2.5 and float(Tuple[0])<5.0:
        Returned6=Returned1+"The average sentiment score is "+str(Tuple[0])+", which means the contents of the tweets on average are overall unhappy."
        return Returned6    #Returns string containing both the general and value dependent statements
    elif float(Tuple[0])>0 and float(Tuple[0])<=2.5:
        Returned7=Returned1+"The average sentiment score is "+str(Tuple[0])+", which means the contents of the tweets on average are overall very unhappy."
        return Returned7    #Returns string containing both the general and value dependent statements
    elif float(Tuple[0])==0:
        Returned8=Returned1+"No tweets containing keywords are present, no conclusion can be drawn"
        return Returned8    #Returns string containing both the general and value dependent statements


### MAIN FUNCTION THAT CALLS OTHER FUNCTIONS ###

def compute_tweets(Tweet_File,Keywords_File):
    Punc=',!@#$%^&*()?<>:;""+=_[]'''
    NORTHERN_BOUNDARY=float(49.189787)
    SOUTHERN_BOUNDARY=float(24.660845)
    RIGHT_EASTERN_TIMEZONE_BOUNDARY=float(-67.444574)
    RIGHT_CENTRAL_TIMEZONE_BOUNDARY=float(-87.518395)
    RIGHT_MOUNTAIN_TIMEZONE_BOUNDARY=float(-101.998892)
    RIGHT_PACIFIC_TIMEZONE_BOUNDARY=float(-115.236428)
    LEFT_PACIFIC_TIMEZONE_BOUNDARY=float(-125.242264)
    Total_Tweet_Counter=0
    Eastern_Total_Tweet_Counter=0
    Central_Total_Tweet_Counter=0
    Mountain_Total_Tweet_Counter=0
    Pacific_Total_Tweet_Counter=0
    Output_List=[]
    Tweets_Table=[]
    Eastern_Tweets_Table=[]
    Central_Tweets_Table=[]
    Mountain_Tweets_Table=[]
    Pacific_Tweets_Table=[]
    Eastern_Tuple=0
    Central_Tuple=0
    Mountain_Tuple=0
    Pacific_Tuple=0
    New_String=""
    New_List=[]
    Total_Tweet_Counter=0
    Output_List=[]
    Empty_List=[]

    try:            #try block- if not able to open either file and therefore perform the function an exception will be raised
        Tweet_File=open(Tweet_File,"r",encoding="utf-8")        #opens file of tweets
        Keywords_File=open(Keywords_File,"r",encoding="utf-8")  #opens file of keywords
        Processed=String_Processor(Tweet_File,Punc)         #Processes tweets
        Processed=Processed.splitlines()            #Splits processed tweets and adds them to a list as elements

        Keywords_Table=Keywords_File_Formatter(Keywords_File)  #Processes file of keywords

        for i in range(0,len(Processed)):           #Iterates over list of tweets
                Processed2=Processed[i].split()     #Takes entries from list,breaks them into words and adds them to a list
                Tweets_Table.append(Processed2)#Adds list to grand list (or table)

        for x in range(0,len(Tweets_Table)):        #Iterates over elements in table (or grand list)
            if float(Tweets_Table[x][0])<=NORTHERN_BOUNDARY and float(Tweets_Table[x][0])>=SOUTHERN_BOUNDARY:       #Determines if it is even possible to fit within a timezone (if not in latitude bounds the longitude bounds are irrelevant)
                if float(Tweets_Table[x][1])<=RIGHT_EASTERN_TIMEZONE_BOUNDARY and float(Tweets_Table[x][1])>RIGHT_CENTRAL_TIMEZONE_BOUNDARY:
                    Eastern_Tweets_Table.append(Tweets_Table[x])       #Adds table elements from master list into a subtable by region
                    Eastern_Total_Tweet_Counter=Eastern_Total_Tweet_Counter+1   #Regional tweet counter
                elif float(Tweets_Table[x][1])<=RIGHT_CENTRAL_TIMEZONE_BOUNDARY and float(Tweets_Table[x][1])>RIGHT_MOUNTAIN_TIMEZONE_BOUNDARY:
                    Central_Tweets_Table.append(Tweets_Table[x])        #Adds table elements from master list into a subtable
                    Central_Total_Tweet_Counter=Central_Total_Tweet_Counter+1   #Regional tweet counter
                elif float(Tweets_Table[x][1])<=RIGHT_MOUNTAIN_TIMEZONE_BOUNDARY and float(Tweets_Table[x][1])>RIGHT_PACIFIC_TIMEZONE_BOUNDARY:
                    Mountain_Tweets_Table.append(Tweets_Table[x])       #Adds table elements from master list into a subtable
                    Mountain_Total_Tweet_Counter=Mountain_Total_Tweet_Counter+1 #Regional tweet counter
                elif float(Tweets_Table[x][1])<=RIGHT_PACIFIC_TIMEZONE_BOUNDARY and float(Tweets_Table[x][1])>=LEFT_PACIFIC_TIMEZONE_BOUNDARY:
                    Pacific_Tweets_Table.append(Tweets_Table[x])        #Adds table elements from master list into a subtable
                    Pacific_Total_Tweet_Counter=Pacific_Total_Tweet_Counter+1   #Regional tweet counter

        #Creating region specific tuples using Average function whose parameters come from Happiness_Calculator
        Value_To_Average=Happiness_Calculator(Eastern_Tweets_Table,Keywords_Table,Eastern_Total_Tweet_Counter)
        Eastern_Tuple=Average(Value_To_Average)
        Value_To_Average2=Happiness_Calculator(Central_Tweets_Table,Keywords_Table,Central_Total_Tweet_Counter)
        Central_Tuple=Average(Value_To_Average2)
        Value_To_Average3=Happiness_Calculator(Mountain_Tweets_Table,Keywords_Table,Mountain_Total_Tweet_Counter)
        Mountain_Tuple=Average(Value_To_Average3)
        Value_To_Average4=Happiness_Calculator(Pacific_Tweets_Table,Keywords_Table,Pacific_Total_Tweet_Counter)
        Pacific_Tuple=Average(Value_To_Average4)

        #Adding regional tuples to list
        Output_List.append(Eastern_Tuple)
        Output_List.append(Central_Tuple)
        Output_List.append(Mountain_Tuple)
        Output_List.append(Pacific_Tuple)

        Total_Tweet_Counter=(len(Eastern_Tweets_Table)+len(Central_Tweets_Table)+len(Mountain_Tweets_Table)+len(Pacific_Tweets_Table))      #Calculation for later use
        Print_Results(Total_Tweet_Counter,Eastern_Tweets_Table,Central_Tweets_Table,Mountain_Tweets_Table,Pacific_Tweets_Table,Output_List,Eastern_Tuple,Central_Tuple,Mountain_Tuple,Pacific_Tuple)   #prints results of calculations utilizing smaller functions

        return Output_List      #Returns list of tuples

    except Exception:       #What is to happen if files cannot be opened or any other issue processing
        print("At least one of your desired files does not exist")
        return Empty_List   #Returns empty list


