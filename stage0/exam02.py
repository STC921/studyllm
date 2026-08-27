#The exam02 is for

import yaml

data = {"name" : "Sam",
        "Age" : 26,
        "score" : [90, 85,80],
        "info" : {
            "city" : "Iwaki",
            "job" : "QA Engineer"
        }
    }

with open("config.yaml", "w", encoding="utf-8") as f:
    yaml.dump(data, f, allow_unicode=True, default_flow_style=False)

with open("config.yaml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)
print(data)
print(data["info"]["city"])

with open("config.yaml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)
data["Age"] = 30
data["info"]["city"] = "Tokyo"
with open("config.yaml", "w", encoding="utf-8") as f:
    yaml.dump(data, f, allow_unicode=True, default_flow_style=False)