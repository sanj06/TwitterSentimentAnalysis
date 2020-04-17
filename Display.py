from DataTable import DataTable
from Graph import Graph

class Display():
        def __init__(self):
                pass
                
        


        def displayResult(self):
                                
                dt = DataTable()  
                          
                table = dt.displayDataTable()
                

        
                g = Graph()
                polarity_value=g.displayGraph()

                table.append(polarity_value)
                return table

                

