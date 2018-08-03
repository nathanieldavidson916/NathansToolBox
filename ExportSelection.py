## Author: Nathan Davidson
## Github: https://www.github.com/nathanieldavidson916

import pymel.core as pm
pm.loadPlugin("fbxmaya") # LOAD PLUGIN

class SelectFiles:
    def __init__(self):
        self.files = None
    def OpenFiles(self):
        self.files = cmds.fileDialog2(fileMode=4)
    def ExportLocation(self):
        self.exportLocation = cmds.fileDialog2(fileMode=3)


x = SelectFiles()
x.OpenFiles()
x.ExportLocation()

for item in x.files:
    FilePath = item
    print(item)
    FileName = item.split('/')[-1:][0].split('.')[0]
    
    cmds.file(FilePath, i=True, namespace=FileName)

Objects = cmds.ls(type="mesh")
for object in Objects:
    exportName = object.split(':')[0]
    cmds.select(object)
    pm.mel.FBXExport(f=x.exportLocation[0]+'/'+exportName, s=True)