#Using dictionary and exception handling


class Solution:
    def duplicates(self, arr, n): 
    	md={}
    	a=[]
    	for element in arr:
    	    try:
    	        md[element]+=1
    	    except:
    	        md[element]=1
    	
    	for item in md:
    	    if md[item]>1:
    	        a.append(item)
    	if len(a)==0:
    	    a.append(-1)
    	a.sort()
    	return a
