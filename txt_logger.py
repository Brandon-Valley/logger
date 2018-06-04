# logger for .txt files

DEFAULT_HEADER_MARK = ': '



# MOST SIMPLE WRITE FUNCTION, MOSTLY HERE FOR EXAMPLE PURPOSES
#
# Original .TXT FILE:  (same output if no file exists)
# 
#     nameA: Harry
#     nameB: Bob
#     nameC: Mark
#     nameD: Captain Falcon
#
# INPUT:
#  
#     logDict = { 'color1': 'Blue',
#                 'color2': 'Green',     
#                 'color3': 'Red'}  
#
#     headerOrderList = ['color1', 'color2', 'color3']    
# 
# Final .TXT FILE:
# 
#     color1: Blue
#     color2: Green
#     color3: Red
#
# creates new file or overwrites existing existing file
def overwriteVarsSimple(filePath, logDict, headerOrderList, headerMark = DEFAULT_HEADER_MARK):
    f = open(filePath, 'w')
    
    for header in headerOrderList:
        line = header + headerMark + logDict[header]
        f.write(line + '\n')
        
    f.close()
    
    
    
    
# Original .TXT FILE:  (same output if no file exists)
# 
#     nameA: Harry
#     nameB: Bob
#     nameC: Mark
#     nameD: Captain Falcon
#
# INPUT:
#  
#     logDict = { 'color1': 'Blue',
#                 'color2': 'Green',     
#                 'color3': 'Dark Red'}  
#
#     headerOrderList = ['color1', 'color2', 'color3']    (optional but without it, order will be random)
# 
# Final .TXT FILE:
# 
#     color1: Blue
#     color2: Green
#     color3: Red
#
# creates new file or overwrites existing file
def overwriteVars(filePath, logDict, headerOrderList = None, headerMark = DEFAULT_HEADER_MARK):
    f = open(filePath, 'w')
    
    if headerOrderList == None:
        for header, value in logDict.items():
            line = header + headerMark + logDict[header]
            f.write(line + '\n') 
    else:
        for header in headerOrderList:
            line = header + headerMark + logDict[header]
            f.write(line + '\n')     
                
    f.close()
    
    
    
    
# INPUT:
#  
#     headerOrderList = ['color1', 'color2', 'color3']    
#         
#     logDict = { 'color1': 'Blue',
#                 'color2': 'Green',     
#                 'color3': 'Red'}  
# 
# .TXT FILE:
# 
#     color1: Blue
#     color2: Green
#     color3: Red
#
# creates new file or overwrites existing existing file
def logVars(filePath, logDict, headerOrderList = None, headerMark = DEFAULT_HEADER_MARK):
    f = open(filePath, 'w')
    
#     for header in headerOrderList:#```````````````````````````````````````````````````````````````````````````````````````````````
#         line = header + headerMark + logDict[header]
#         f.write(line + '\n')

    if headerOrderList == None:
        for header, value in logDict.items():
            line = header + headerMark + logDict[header]
            f.write(line + '\n') 
    else:
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

    
    
    
    
    
def editVars(filePath, logDict, headerMark = DEFAULT_HEADER_MARK):
    ogLogDict, headerOrderList = readVars(filePath, True, headerMark = DEFAULT_HEADER_MARK)
    
    
    
    
    
filename0 = 'examples/txt_logger_examples/colorList.txt'
   
headerOrderList0 = ['color1', 'color2', 'color3']    
    
logDict0 = {'color1': 'Blue',
            'color2': 'Green',     
            'color3': 'Dark Red'}

    
filename1 = 'examples/txt_logger_examples/nameList.txt'

logDict1 = {'nameA': 'Harry',
            'nameB': 'Bob',
            'nameC': 'Mark',
            'nameD': 'Captain Falcon'}



logVars(filename0, logDict0, headerOrderList0)
logVars(filename1, logDict1,)

resultDict0, resultHeaderOrderList0 = readVars(filename0, True)
print('resultDict0: ', resultDict0)
print('resultHeaderOrderList0: ', resultHeaderOrderList0)
print('')

resultDict1 = readVars(filename1)
print('resultDict1: ', resultDict1)
print('')

print('done!')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    