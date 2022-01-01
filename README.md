# gosper_glider_gun

Conway's Game of Life via Spatial Analyst

```python
def tick(grid):
  g = FocalStatistics(grid, NbrRectangle(3, 3), "SUM", "DATA") - grid
  return (grid == 1) & (g == 2) | (g == 3)
```
https://user-images.githubusercontent.com/3728748/147857636-740118f3-7874-4c36-8476-04ab55e72418.mp4
