import arcpy, os, glob
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")

def tick(grid):
  g = FocalStatistics(grid, NbrRectangle(3, 3), "SUM", "DATA") - grid
  return (grid == 1) & (g == 2) | (g == 3)

f = os.getcwd()

grid = Int(arcpy.ASCIIToRaster_conversion(f + "\\life.txt"))

for i in range(1, 100):
  grid = tick(grid)
  grid.save(f + "\\" + str(i).rjust(2, "0") + ".tif")

arcpy.RasterToOtherFormat_conversion(glob.glob(f + "\\*.tif"), f, "BMP")
arcpy.RasterToVideo_conversion(f, "life.avi", "BMP", "Microsoft Video 1", "TIME", "12")
