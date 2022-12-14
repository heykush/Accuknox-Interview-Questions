import json

restaurant_logs = []
restaurant_logs_exception_case = []
with open("test_case.json", "r") as file:
    restaurant_logs = json.load(file)

with open("test_case_exception.json", "r") as file:
    restaurant_logs_exception_case = json.load(file)

def check_if_same_eater_id_has_ordered_twice(logs):
    eater_ids = {}
    for log in logs:
        if log["eater_id"] not in eater_ids:
            eater_ids[log["eater_id"]] = [log["food_menu_id"]]
        else:
            if log["food_menu_id"] in eater_ids[log["eater_id"]]:
                return [True, log["eater_id"], log["food_menu_id"]]
            eater_ids[log["eater_id"]].append(log["food_menu_id"])
    return [False]

def get_top_three_menu_items(logs):
    menu_items = {}
    if check_if_same_eater_id_has_ordered_twice(logs)[0]:
        raise Exception("Eater ID: {} has ordered twice".format(check_if_same_eater_id_has_ordered_twice(logs)[1]))
    for log in logs:
        if log["menu_item"] not in menu_items:
            menu_items[log["menu_item"]] = 1
        else:
            menu_items[log["menu_item"]] += 1
    top_three = sorted(menu_items.items(), key=lambda x: x[1], reverse=True)[:3]
    return [item[0] for item in top_three]

top_threee = get_top_three_menu_items(restaurant_logs).__str__().strip("[]").translate(str.maketrans('', '', "'"))
print(f"The top three menu items are: {top_threee}")
top_threee_exception_case = get_top_three_menu_items(restaurant_logs_exception_case).__str__().strip("[]").translate(
    str.maketrans('', '', "'"))
print(f"The top three menu items are: {top_threee}")
