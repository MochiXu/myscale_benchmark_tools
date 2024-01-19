## Note
This repo is a script tool for update [myscale/benchmark](https://github.com/myscale/benchmark) results.
1. You can use [handle_price.py](./handle_price.py) to add a `price` field to the results you are testing.
2. Use the `handle_probability.py` script to process datasets of the filter type. 
For instance, if you have tested the `laion5m_prob` dataset using the `vector-db-benchmark`, 
the test results for different filter ratios (such as 0.001, 0.01, 0.1) will be stored in the `vector-db-benchmark/results` folder. 
To align with the display logic of the [myscale/benchmark](https://github.com/myscale/benchmark) frontend page, 
we utilize the `handle_probability.py` script to update all json files in this `results` folder. 
Suppose we have results for the `myscale` engine on the `laion5m_prob` dataset for filter ratios of 0.001, 0.01, and 0.1 in the `results` folder. 
After processing this folder with the `handle_probability.py` script, we will obtain three separate folders: `results-0.001`, `results-0.01`, and `results-0.1`. 
These folders are then to be further processed by the `handle_benchmark_results.py` script.
3. Provide the paths of all JSON files that need to be visualized to the handle_benchmark_results.py script. 
By executing this script, the final benchmark.json file will be generated. 
Use this file to update the test results on the [myscale/benchmark](https://github.com/myscale/benchmark/blob/main/public/benchmark.json). 
This process will complete the update of the frontend data results.

## Others
During the testing process with `vector-db-benchmark`, some issues are inevitable. 
For instance, a test case might successfully execute during the upload stage but then unexpectedly exit during the search stage. 
To save time in such situations, we directly execute `python3 run.py --skip-upload` to skip the case upload stage. 
However, this leads to the absence of upload information in the results file. 
We need to manually complete this information afterward by using [handle_upload_data.py](./handle_upload_data.py).