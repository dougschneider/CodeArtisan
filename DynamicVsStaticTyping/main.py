from Room import Room
from Table import Table

room = Room();
firstTable = Table("table one")
firstTable.seatPlayer("James")
firstTable.seatPlayer("Brian")
firstTable.seatPlayer("Joel")
room.addTable(firstTable)
secondTable = Table("table two")
secondTable.seatPlayer("Sarah")
secondTable.seatPlayer("William")
secondTable.seatPlayer("Lauren")
secondTable.seatPlayer("Alyssa")
room.addTable(secondTable)

room.printTables()
