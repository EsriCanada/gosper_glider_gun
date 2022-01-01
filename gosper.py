import arcpy, os, cv2
from arcpy import env
from arcpy.sa import *
from datetime import datetime

# Check out Spatial Analyst.
arcpy.CheckOutExtension("Spatial")

# Workspace.
root = os.getcwd()
env.workspace = os.path.join(root, datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
os.mkdir(env.workspace)

# Parameters.
inputFile = os.path.join(root, "gosper.txt")
outputFile = os.path.join(root, "gosper.mp4")
iterations = 30

# Conway's Game of Life via Spatial Analyst.
def tick(grid):
  g = FocalStatistics(grid, NbrRectangle(3, 3), "SUM", "DATA") - grid
  return (grid == 1) & (g == 2) | (g == 3)

# Import the seed raster.
grid = Int(arcpy.ASCIIToRaster_conversion(inputFile))

# Process.
for i in range(1, iterations + 1):
    print (f"Processing {i} of {iterations}")   
    path = os.path.join(env.workspace, str(i).rjust(3, "0"))

    # Generate, save and reload.  This is a workaround for the performance issue.
    tick(grid).save(path)
    grid = Raster(path)

    # Stretch, resample and save.
    Resample(SetNull(grid == 0, 255), "NearestNeighbor", 1000, 100).save(f"{path}.tif")

# Generate a video from the tif files.
images = [img for img in os.listdir(env.workspace) if img.endswith(".tif")]
frame = cv2.imread(os.path.join(env.workspace, images[0]))
h, w, _ = frame.shape
video = cv2.VideoWriter(outputFile, 0, 10, (w, h))

for image in images:
    video.write(cv2.imread(os.path.join(env.workspace, image)))

cv2.destroyAllWindows()
video.release()

# Play the video.
os.startfile(outputFile, "open")
