# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 11:04:08 2019

@author: sophia
"""


from operator import itemgetter
class Gene :
    """ Class that holds the attributes of a gene"""
    
    def __init__(self,filename):
        """constructs a new Gene object by initializing the attribute filename
        that stores the nucleotides of genetic codes"""
        file = open(filename)
        reading = file.readline() # reads first line of file
        firstline = reading.split()
        name = firstline[1]+ ' '+ firstline[2] # gives the scientific name of the organism
        #print(name)
        codes = file.readlines() # reads all the lines of the file
        init_code = codes[2:] # assigns the genetic code to the variable 'gen_code'
        
        gen_code = ''
        seq = ''
        
        for line in init_code:
            if line[-1] == '\n':
                line = line[:-1]
            gen_code = line.strip()
           
            for lines in gen_code:
                seq += lines
                        
        
        self.name = name
        self.seq = seq
    
    def __repr__(self):
        return self.name + ', '+ self.seq
        
        
    def similarity_difference(self,other):
        """looks at the similarity between 2 codes
        """
        percent = self.check_seq(other.seq)[0:5]
        if len(self.seq) > len(other.seq):  #Finding the difference between the length of the two text files
            d1 = len(self.seq) - len(other.seq)
        elif len(self.seq) < len(other.seq):
            d1 = len(other.seq) - len(self.seq)
        else:
            d1=0
        return percent + "% Similarity between "+ self.name + " and "+ other.name + " , " + str(d1) + " Difference in length"
    
    def check_seq(self, seq):
        """looks at the similarity between 2 codes
        """
        count_similar = 0
        count_total = 0     
        if len(self.seq) < len(seq): # We use the shorter element to iterate through each line
            file = len(self.seq)
        else:
            file = len(seq)
        for i in range(0, file): #Checks each element and adds amount of times the code is similar
            if self.seq[i] == seq[i]:
                count_similar += 1
            count_total += 1
            #print(txt1[i],' ', txt2[i], '\n')
        if len(self.seq) > len(seq):  #Finding the difference between the length of the two text files
            d1 = len(self.seq) - len(seq)
        elif len(self.seq)<len(seq):
            d1 = len(seq) - len(self.seq)
        else:
            d1=0
            
        #return count_similar           
        percent = (count_similar/count_total) * 100      
        return str(percent) + "% Similarity between "+ self.name + " and the mutated code " + " , " + str(d1) + " Difference in length"
        
    def comparision(self,filelist):
        for file in filelist:
            obj = Gene(file)
            a = self.similarity_difference(obj)
            print(a)
    
    def listing(self,filelist):
        obj1 = Gene(filelist[0])
        name_percent = []
        for file in filelist[1:]:
            obj = Gene(file) # gets a gene object from the file
            val = float(obj.similarity_difference(obj1)[0:5]) # takes the first element of the list and compares it with the rest of the elements from the similiarity difference function
            name_percent.append([val,obj.name]) # creates a list of lists with the percentage similiarity and the name
        name_percent = sorted(name_percent, key=itemgetter(0), reverse=True) # sorts the list by the first element of the list
        return name_percent
        
    def showindow(self):
        self.mainwindow.title("Emergence Grid")
        self.mainwindow.geometry("500x500") # default size of the window
        self.mainwindow.resizable(0, 0)
        self.mainwindow.bind('<Button-1>', self.onMouseClick) # bind the onMouseClick to the left mouse click <Button-1>
        # make the application ready to run. mainloop() is an infinite loop used to run the application, wait for an event to occur and process the event till the window is not closed.
        self.mainwindow.mainloop()
      
            
    
if __name__ == "__main__":
    filelist = ['Aquirufa.fasta','bacillus.fasta','bacteriodes.fasta','e.coli.fasta']
    #ilelist = ['Aq'sequence2.txt','sequence.txt','sequence2.txt']
    a = Gene('sequence.fasta')
    a.comparision(filelist)
    print(a.listing(filelist))
    







