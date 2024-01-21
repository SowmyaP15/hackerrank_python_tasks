# Multiset Implementation: multiset.py

# Python3 program from python multiset implementation

given a template for the multisite class, implement 4 methods: 
1) add(self , val) : adds value to the multisite
2) remove (self, val) : if val is in the multiset, removes val from the multisite otherwise do nothing
3) __contains__(self, val): returns true if val is in the multiset; otherwise, it returns false
4) __len__(self) : returns the number of elements in the multiset

Additional methods are allowed as necessary.
the implementation of the 4 required methods will be tested by a provided code stub on several input files, each input file contains several operations, each of one of the below types.

complete the class multiset with the 4 methods given (add, remove, __Contains__ and __len__).
constraints: 
1) 1 <= number of operations in one test file <= 10 power 5
2) if val is parameter of operation then val is an integer and 1 <= val <=10 power 9

# Vending Machine Program: vendingmachine.py

Python3 program from vending machine :
implement class : vending machine according to the following requirements:
1) can be instantiated using the constructor vending machine(num_items,item_price)
where num_items denotes the number of items in the machine and item_price denotes the required number of coins to buy a single item
2) has a method buy(req_items,money) that represents a buy request where req_items denotes the requested number of items and money is the amount customer puts into the machine.
Depending on the state of the machine one of the following happens:
1) if there are enough items in the machine to serve the request and the given money is sufficient to buy the requested number of items the number of items in the machine is reduced by the requested number of items.The method returns and integer denotes the change given back after the purchase.
2) If there are fewer items in the machine than the requested number it raises value error exception with the message "not enough items in the machine".
3) if there are enough items in the machine to serve the request but the given amount of money is less than their cost, it raises a value error exception with the message "Not enough coins".
The class implementation will be tested by a provided code stub and several input files. Each input file contains parameters to test the implementation. First the provided code stub initializes an instance of the vending machine. Next it performs the given operations on the vending machine instance. the result of their execution will be printed to the standard output provided by the code.
constraints:
there will be atmost 100 operations to be performed
