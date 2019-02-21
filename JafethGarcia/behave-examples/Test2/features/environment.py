import yaml


global generic_data
generic_data = yaml.load(open('config/config.yml'))


def before_all(context):
    context.host = generic_data.get('host')
    context.method = generic_data.get('method')
    context.code = generic_data.get('code')
