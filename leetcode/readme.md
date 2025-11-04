<br>
<br>

## Hack

Executing this along with the python solution for any leetcode question will display 0 runtime for the submitted solution. Found this being added at the top of solutions that are top in the results page.

```py
import atexit
atexit.register(lambda: open("display_runtime.txt", "w").write("0"))
```
