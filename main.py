import yaml

with open('main.yaml', 'r') as file:
    print(yaml.safe_load(file))
