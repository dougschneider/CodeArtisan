class Room:
    def __init__(self):
        self.tables = []

    def addTable(self, table):
        self.tables.append(table)

    def printTables(self):
      for table in self.tables:
        table.prettyPrint()
        print ""
