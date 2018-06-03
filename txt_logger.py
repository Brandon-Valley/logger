# logger for .txt files

DEFAULT_HEADER_MARK = ': '


# INPUT:
#  
#     headerOrderList = ['color1', 'color2', 'color3']    
#         
#     logDict = { 'color1': 'Blue',
#                 'color2': 'Green',     
#                 'color3': 'Red'}  
# 
# TXT FILE:
# 
#     color1: Blue
#     color2: Green
#     color3: Red
def logVars(filePath, logDict, headerOrderList, headerMark = DEFAULT_HEADER_MARK):
    f = open(filePath, 'w')
    
    for header in headerOrderList:
        line = header + headerMark + logDict[header]
        f.write(line + '\n')
        
    f.close()
    
    

# INPUT .TXT FILE:
#
#     color1: Blue
#     color2: Green
#     color3: Red
#
#
#
# OUTPUT:   (if wantHeaderOrderList == True)
#  
#      (  logDict = { 'color1': 'Blue',     ,     headerOrderList = ['color1', 'color2', 'color3']  )
#                     'color2': 'Green',     
#                     'color3': 'Red'}  
# 
# OTHERWISE, OUTPUT:
#
#     logDict = { 'color1': 'Blue',
#                 'color2': 'Green',     
#                 'color3': 'Red'} 
#
def readVars(filePath, wantHeaderOrderList = False, headerMark = DEFAULT_HEADER_MARK):
    logDict = {}
    headerOrderList = []
    
    with open(filePath) as textFile:  # can throw FileNotFoundError
        raw_lines = tuple(l.rstrip() for l in textFile.readlines())
        
    for line in raw_lines:
        header, value = line.split(headerMark)
        
        headerOrderList.append(header)
        logDict[header] = value
        
    textFile.close()
        
    if wantHeaderOrderList == True:
        return (logDict, headerOrderList)
    else:
        return logDict

    
    
    
    
    
    
    
    
headerOrderList = ['color1', 'color2', 'color3']    
    
logDict = { 'color1': 'Blue',
            'color2': 'Green',     
            'color3': 'Red'}


filename = 'colorList.txt'

logVars(filename, logDict, headerOrderList)

resultDict, resultHeaderOrderList = readVars(filename, True)
print('resultDict: ', resultDict)
print('resultHeaderOrderList: ', resultHeaderOrderList)
print('done!')
    
    
    