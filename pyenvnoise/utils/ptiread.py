
import numpy as np

def ptiread(file_name):
    
    fid = open(file_name, "r")
    
    headerlinecnt = 1
    numref = 1
    
    ## Get all information
    # get hearder information setup
    # first 15 lines are setup info
    
    tline = fid.readline()
    
    # determine start header line
    while tline != '[SETUP START]\n':
        numref += 1
        headerlinecnt += 1
        end_setup = numref + 13
        tline = fid.readline()

    
    while headerlinecnt<end_setup:
        tline = fid.readline()
            
        headerlinecnt = headerlinecnt + 1
        if headerlinecnt == (numref+2):
           RECInfoSectionSize = int(tline.partition('=')[2])
           
        if headerlinecnt == (numref+3):
            RECInfoSectionPos = int(tline.partition('=')[2])
     
        if headerlinecnt==(numref + 4):
            SampleFrequency = int(float(tline.partition('=')[2]))
         
        if headerlinecnt==(numref+5):
            numchannels = int(tline.partition('=')[2])
            
        if headerlinecnt==(numref+11):
            Sample = int(tline.partition('=')[2])
        
        if headerlinecnt==(numref+12):
            Date = tline.partition('=')[2]
        
        if headerlinecnt==(numref+13):
            Time = tline.partition('=')[2]
            
    ## Get channel info
    # the most important infor is correction factor
    CorrectionFactor = []
    for nchann in range(numchannels):
        for i in range(10):
            
            tline = fid.readline()
            
            if tline.partition('=')[0] == 'CorrectionFactor':
                CorrectionFactor.append(float(tline.partition('=')[2]))
                
            if tline.partition('=')[0] == 'SampleFrequency':
                SampleFrequency = int(tline.partition('=')[2])
        
        
    ## Read binary data
    # poiter to main data
    # 20 bytes may a subheader which may not important
    fid.seek( RECInfoSectionPos + RECInfoSectionSize + 20, 0)
    
    # the size of each segment, it around 250 ms
    # fro Fs = 8192 Hz, it is 2048*4 bytes data + 4*4 bytes info (channel id)
    dsize = np.fromfile(fid, dtype=np.int16, count=1)
    cols = int(Sample/(dsize-4)*numchannels)
    
    # back to start data
    fid.seek( RECInfoSectionPos + RECInfoSectionSize + 20, 0)
    #print(fid.tell())
    
    # read all data into rawdata and ignore 4 first bytes with info
    rawdata = np.fromfile(fid, np.int32).reshape((-1, dsize[0])).T
    rawdata = np.delete(rawdata, np.s_[0:4], 0)
    
    ## Save data into channels
    # calculate factors for actual Pa, full range is 16 bit system
    CorrectionFactor = np.array(CorrectionFactor)
    factor = CorrectionFactor / 2**16
    
    # initilise array data
    Data = np.empty([int(rawdata.shape[0]*rawdata.shape[1]/numchannels), numchannels])
    
    
    for i in range(numchannels):
        Data[:,i]= np.transpose( rawdata[:,i:rawdata.shape[1]:numchannels] ).ravel()*factor[i]
        
    return Data, SampleFrequency, Date, Time
        
        
        
#data = ptiread('R:\CMPH-Windfarm Field Study\Hallett\set2\Recording-1.4.pti')
        
        
        
    
