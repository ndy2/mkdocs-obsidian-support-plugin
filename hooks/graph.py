import os
import json
import re
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import Files

pattern = re.compile(r"(?<!\!)\[\[([^|^\]^#]+)\]\]")

def get_file_name(name: str):
    return name if name != 'index' else 'Home'

def create_graph_json(files: Files, config: MkDocsConfig):
    data = json.loads('{ "nodes": [], "links": [] }')
    nodes = {}
    for file in files:
        if file.is_documentation_page():
            name = get_file_name(file.name)
            nodes[name] = {
                "url": file.url
            }
            nodes[name]["symbolSize"] = nodes[name].get("symbolSize", 0)

            for line in open(file.abs_src_path):
                for match in re.finditer(pattern, line):
                    link = { 
                        "source": name,
                        "target": match.group(1)
                    }
                    data["links"].append(link)
                    nodes[name]["symbolSize"] = nodes[name].get("symbolSize", 1) + 1

    for k,v in nodes.items():
        node = {
                "name": k,
                "symbolSize": v["symbolSize"],
                "value": v["url"]
        }
        data["nodes"].append(node)

    with open(os.path.join(config['site_dir'], 'data.json'), 'w') as f:
        json.dump(data, f, sort_keys=False, indent=2)

def on_files(files: Files, config: MkDocsConfig, **kwargs):
    create_graph_json(files, config)