# gosper_glider_gun

Conway's Game of Life via Spatial Analyst

```python
def tick(grid):
  g = FocalStatistics(grid, NbrRectangle(3, 3), "SUM", "DATA") - grid
  return (grid == 1) & (g == 2) | (g == 3)
```

<img src="https://github.com/EsriCanada/gosper_glider_gun/blob/master/demo.gif?raw=true" width="300">
