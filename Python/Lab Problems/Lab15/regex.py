def rowz(s):
        top = ""
        middle = ""
        bottom = ""
        for i in range(0,len(s), 4):
            top += s[i] + '   '
            
        for i in range(2, len(s), 4):
            bottom += s[i] + '   '
            
        for i in range(1, len(s), 2):
            middle += s[i] + ' '
        
        print('{}\n{}\n{}'.format(top, middle, bottom))
        
rowz("PAYPALISHIRING")