import json

with open("sample-data.json", "r") as file:
    data = json.load(file)
    
print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':10}")
print("-" * 50 + " " + "-" * 20 + " " + "-" * 8 + " " + "-" * 6)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes.get("dn")
    descr = attributes.get("descr")
    speed = attributes.get("speed")
    mtu = attributes.get("mtu")
    
    print(f"{dn:<50} {'':<20} {speed:<10} {mtu:<10}")