import json
import os
from typing import Iterator


def walk_result_file_paths(root_path: str) -> Iterator[str]:
    for cur_root_dir_path, cur_dir_names, cur_file_names in os.walk(root_path):
        if len(cur_file_names) != 0:
            for file in cur_file_names:
                if file.endswith(".json"):
                    yield "{}/{}".format(cur_root_dir_path, file)
                else:
                    print("skip invalid file: {}".format("{}/{}".format(cur_root_dir_path, file)))


for file in walk_result_file_paths(root_path="./benchmark_results/CloudTest_v0.0.4_github_benchmark/zilliz_2024_4_3_4cu_performance_optimize"):
    with open(file, 'r') as f:
        data = json.load(f)

    data['meta']['monthly_cost'] = 458.66
    data['meta']['engine']['name'] = 'zilliz-2024-04-03-performance-4cu'
    # data['meta']['engine']['commit'] = 'sha256:5e79bcbd77d08c7730e00bf26f04743c7670b7450c72cb589d82ad1fe4a399fb'
    # data['meta']['engine']['link'] = 'https://hub.docker.com/r/tensorchord/pgvecto-rs/'
    # data['meta']['engine']['remark'] = 'tensorchord/pgvecto-rs:pg15-v0.0.0-nightly.20231018-amd64'

    with open(file, 'w') as f:
        json.dump(data, f, indent=2)
