from assertpy.assertpy import assert_that
import pydash


"""Loads and reds value from config.yaml"""

def prop(context, yaml_prop) -> str:
    assert_that(yaml_prop, 'YAML Property is required').is_not_none().is_not_empty()
    yaml_prop_value = pydash.get(context, yaml_prop)
    assert_that(yaml_prop_value, f'YAML Property not found: {yaml_prop}').is_not_none().is_not_empty()
    print(f'Property: [{yaml_prop}] = [{yaml_prop_value}]')
    return yaml_prop_value


def prop_file_content(context, yaml_file_prop) -> str:
    yaml_prop_value = prop(context, yaml_file_prop)
    assert_that(yaml_prop_value, f'File Not Found - {yaml_file_prop} : {yaml_prop_value}').exists()
    with open(yaml_prop_value) as f:
        return f.read()
