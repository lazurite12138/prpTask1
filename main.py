import sys
from PyQt5.QtWidgets import QApplication,QWidget
from ui.YCYMainWindow import YCYMainWindow
import pydicom

if __name__=="__main__":
    # app=QApplication(sys.argv)
    #
    # mainWindow = YCYMainWindow()
    # mainWindow.show()
    # sys.exit(app.exec_())

    ds = pydicom.read_file("E:/prp/test_data/Patient_Test_data/MRIDicom_for_download_1/gre_scout_20200725_150825/00000001.dcm")
    for key in ds.dir():
        Tag_ID=ds[key].tag
        VR=ds[key].VR
        VM=ds[key].VM
        value=ds[key].value
        print("%s   %s  %s  %s  %s" %(Tag_ID,VR,VM,key,value))