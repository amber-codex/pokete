import sys
import os
import pytest     
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pokete_data import maps     
from pokete_data import map_data 
 
new_maps = [ "playmap_52","playmap_55", "playmap_56", "playmap_57"]
@pytest.mark.parametrize("map_name", new_maps)
def test_map_definitions_exist(map_name):
    assert map_name in maps.keys() # asseter the new map is on the maps file

@pytest.mark.parametrize("map_name", new_maps)
def test_map_attributes(map_name):
    required_attributes = ["weather","height","width","song","pretty_name","extra_actions","poke_args"]
    map_obj = maps[map_name]
    assert map_obj is not None
    objs = map_obj
    for dict_attr in map_obj:
        if type(dict_attr) == dict:
            objs += list(dict_attr.keys())
    for current_req in required_attributes:
        assert current_req in objs
            
@pytest.mark.parametrize("map_name", new_maps)           
def test_objects(map_name):
    maps_check_y = maps[map_name]["height"]
    maps_check_x = maps[map_name]["width"]
    def extract_dictionaries(nested_dict, result=None):
        if result is None:
            result = []

        # Check if the current object is a dictionary
        if isinstance(nested_dict, dict):
            result.append(nested_dict)  # Add the current dictionary to the result
            for key, value in nested_dict.items():
                # Recursively process nested dictionaries
                extract_dictionaries(value, result)

        return result
    
    separated_dicts = extract_dictionaries(map_data[map_name])
    print(map_name)
    print(separated_dicts)
    for i in range(len(separated_dicts)):
        if "x" in separated_dicts[i].keys() and "y" in separated_dicts[i].keys() and 'args' not in separated_dicts[i].keys() and'map' not in separated_dicts[i].keys():
            test_x = separated_dicts[i]["x"]
            test_y = separated_dicts[i]["y"]
            statement = test_x <= maps_check_x and test_y <= maps_check_y
            print(test_y, maps_check_y)
            print(test_x,maps_check_x)
            print(separated_dicts[i])
            print(test_x <= maps_check_x and test_y <= maps_check_y)
            assert statement
