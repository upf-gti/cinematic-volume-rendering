from mevis import *
from PythonQt import QtCore, QtGui
import csv
import itertools
import numpy as np

def expandDirectoryName():
  exp = ctx.expandFilename(ctx.field("source").stringValue())
  dir = MLABFileDialog.getExistingDirectory(exp, "Open directory", MLABFileDialog.ShowDirsOnly)
  if dir:
    ctx.field("source").value = ctx.unexpandFilename(dir)
    ctx.field("DirectDicomImport.source").value = ctx.unexpandFilename(dir)

def importData():
  ctx.field("DirectDicomImport.dplImport").touch()

def clearLog():
  ctx.field("DirectDicomImport.clearConsole").touch()
  ctx.field("DirectDicomImport.clearDcmTreeCache").touch()
  ctx.field("DirectDicomImport.clearVolumeList").touch()

def init():
  print("Application started... ")
  ctx.field("FieldListener.inParameter").value = "Preset1"
  print(ctx.field("FieldListener.inParameter").value)
  ctx.field("RunPythonScript1.finalize").touch()

def onTFChange(field):
  ctx.field("FieldListener.inParameter").value = ctx.field("LUTs").value
  ctx.field("RunPythonScript1.finalize").touch()

def onCutEnable(field):
  ctx.field("SoVolumeCutting.enabled").value = ctx.field("cutEnable").value

def clipAction(field):
  action = ctx.field("cutAddMode").value
  if action=="Add":
    ctx.field("SoVolumeCutting.cutMode").value = "RemoveExterior"
    ctx.field("SoVolumeCutting.addMode").value = "AlwaysAdd"
  if action=="Subtract":
    ctx.field("SoVolumeCutting.cutMode").value = "RemoveInterior"
    ctx.field("SoVolumeCutting.addMode").value = "AlwaysAdd"

def onChangingLights(field):
  light = ctx.field("Lighting").value
  if light==True:
    ctx.field("SoPathTracerBackgroundLight1.useIBL").value = False
  if light==False:
    ctx.field("SoPathTracerBackgroundLight1.useIBL").value = True

