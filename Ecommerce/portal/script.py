from .models import MainMenu, SubMenu

data = [
    {"AppUrl": "CommonSetup/UOM", "MenuName": "UOM", "ChildMenu": []},
    {"AppUrl": "CommonSetup/Country_Currency", "MenuName": "Country Currency", "ChildMenu": []},
    {"AppUrl": "CommonSetup/Role", "MenuName": "Role", "ChildMenu": []},
    {"AppUrl": "CommonSetup/Master", "MenuName": "Master", "ChildMenu": []},
    {"AppUrl": "CommonSetup/Product Brand", "MenuName": "Product Brand", "ChildMenu": []}
]

for item in data:
    main_menu = MainMenu.objects.create(
        AppUrl=item["AppUrl"],
        MenuName=item["MenuName"]
    )

    for child_menu_data in item["ChildMenu"]:
        SubMenu.objects.create(
            main_menu_ref_id=main_menu,
            AppUrl=child_menu_data["AppUrl"],
            MenuName=child_menu_data["MenuName"]
        )
