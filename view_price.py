import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


PATH = "data_price_CELYAD"

def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)

    return bytesconverter



def loaddata(path):
    try:
        with open(path,"rU") as file :

            Date, Open, High, Low, Close, Volume, Adj = np.loadtxt(file,
                                                                delimiter=",",
                                                                unpack='True', skiprows = 1,
                                                                converters={0: bytespdate2num("%Y-%m-%d")},
                                                                )
        retern = (Close[0:-1]-Close[1::])/ Close[0:-1]

        fig = plt.figure()
        ax1 = plt.subplot(1,1,1)
        ax1.plot(Date[1::],retern)
        plt.show()

        np.savetxt("return_Celyad",(Date[1::],retern),delimiter=",",header="Date,Diff_price" ,newline='\n',)
    except Exception as ex :
        print (ex)





if __name__ == "__main__":
    loaddata(PATH)