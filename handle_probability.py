import json
import os
from utils import walk_result_file_paths

from_path = "./benchmark_results/CloudTest_v0.0.4_github_benchmark/zilliz_2024_4_3_1cu_capacity_optimize/1cu_capacity/laion5m_prob"

for file in walk_result_file_paths(root_path=from_path):
    with open(file, 'r') as f:
        data = json.load(f)
    if file.find("search") == -1:
        continue
    try:
        probability = data['index_search_parameter']['query_meta']['probability']
        data['meta']['dataset'] = f"laion-768-5m-ip-probability-{probability}"
        data['meta']['dataset_tag'] = f"ratio-{probability}"
        # save updated result.
        print(f"{from_path}-{probability}/{file.split('/')[-1]}")
        if not os.path.exists(f"{from_path}-{probability}"):
            os.makedirs(f"{from_path}-{probability}")
        with open(f"{from_path}-{probability}/{file.split('/')[-1]}", 'w') as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print(e)
