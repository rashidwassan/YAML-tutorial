import yaml

# this to check the yaml file contents.
with open('main.yaml', 'r') as file:
    # you will se how the data is converted in json type
    print(yaml.safe_load(file))
