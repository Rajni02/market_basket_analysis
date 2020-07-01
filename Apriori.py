#Implementing useful modules
from itertools import combinations, chain

# rules function provide the association rule between the element
def assoc_rules(f_itemset,C1, min_confidence):
	rules = list()
	for keys in f_itemset:
		#print(keys)
		min_count = f_itemset[keys]
		key = keys.split() 
		if len(key) > 1:
			for A in subsets(key):
				A1=list(A)
				#print(A1[0])
				B = set(key) - set(A)
				if B:
					confidence = float (min_count / C1[A1[0]])*100
					if confidence >= min_confidence:
						rules.append((A1[0], B, confidence))
	return rules



# determine the subset of elementS
def subsets(item):
    return chain(*[combinations(item, i + 1) for i, a in enumerate(item)])

# Count_frequent_item_set determine the occurence of element    
def Count_frequent_item_set(itemset): 
    file = open('exam.txt')
    L = dict()

    for line in file:
        list_line = str(line.split(' '))
        for i in range (0,len(itemset)):
            key = str(itemset[i])
            if key not in L:
                L[key] = 0
            flag = True
            for k in key:
                if k not in list_line:
                    flag = False
            if flag:
                L[key] += 1
    file.close()
    return L

# create L list, occurence of element in L list is greater than minsupport
def Append(Ck,MinSupport):
    L = []
    for i in Ck:
        if Ck[i] >= minsupport:
            L.append(i)
    return sorted(L)

# apriori_gen algo perform join operation
def apriori_gen(frequent):
  
    Itemset = []
   
    for i in range (0,len(frequent)):
        item_1 = str(frequent[i])
        for j in range (i+1,len(frequent)):
            item_2 = str(frequent[j])
            if item_1[0:(len(item_1)-1)] == item_2[0:(len(item_2)-1)]:
                    union = item_1[0:(len(item_1)-1)]+item_2[len(item_2)-1] + item_1[len(item_1)-1] #Combine (k-1)-Itemset to k-Itemset 
                    union = ' '.join(sorted(union))  #Sort itemset by dict order
                    Itemset.append(union)

    return Itemset




#-----------------------------------Main --------------------------------------
if __name__ == '__main__':

	print('--------------------------------------------------------------------------------')
	print( "\nEnter the integer value of minimum support (in integer):")
	minsupport = int(input())

	# File Reading
	with open('exam.txt' , 'r') as f:
  		file = f.read()

	C_1={}
	k=1
	for line in file:
	    for item in line.split():
	        if item in C_1:
	            C_1[item] +=1
	        else:
	            C_1[item] = 1

	L1 = Append(C_1,minsupport)
	L = apriori_gen(L1)

	print ('\n')
	print(' C 1  ', C_1)
	#print(' L1 ',L)
	print ('Frequent itemset of size', k ,'  ',L1)
	k+=1
	C = dict()
	while len(L) >1:
	    #C = dict()
	    C = Count_frequent_item_set(L)
	    frequent_itemset = []
	    frequent_itemset = Append(C,minsupport)
	    L = apriori_gen(frequent_itemset)
	    print ('--------------------------------------------------------------------------------')
	    print(' C',k,'  ', C)
	    #print(' L1 ',L)
	    print ('Frequent',k,'-itemset is',frequent_itemset)
	    k += 1
	print('--------------------------------------------------------------------------------\n')
	print("Enter the confidence interval (in percentage):")
	min_count = int(input())

	print("----------------------------Association Rule---------------------------------\n")
	print('Association Rules are :  ')
	rules  = assoc_rules(C,C_1, min_count)
	for i in rules:
		print(i[0],'-->',i[1], '\t', 'Confidence -level', i[2])