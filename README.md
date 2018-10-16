# gosper_glider_gun

Conway's Game of Life via Spatial Analyst

```python
def tick(grid):
  count = FocalStatistics(grid, NbrRectangle(3, 3), "SUM", "DATA") - grid
  return Con((count == 3) | ((grid == 1) & (count == 2)), 1, 0)
```

<img src="https://github.com/EsriCanada/gosper_glider_gun/blob/master/demo.gif?raw=true" width="300">
