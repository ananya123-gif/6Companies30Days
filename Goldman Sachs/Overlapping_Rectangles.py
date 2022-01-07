#Solution of Overlapping Rectangles

class Solution:
    
    def doOverlap(self, L1, R1, L2, R2):
        #code here
        if(L1[0]>R2[0] or L2[0]>R1[0] or R2[1]>L1[1] or R1[1]>L2[1]):
            return 0
        else:
            return 1
