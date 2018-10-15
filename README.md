# gosper_glider_gun

```python
def tick(grid):
  count = FocalStatistics(grid, NbrRectangle(3, 3), "SUM", "DATA") - grid
  return Con((count == 3) | ((grid == 1) & (count == 2)), 1, 0)
```
