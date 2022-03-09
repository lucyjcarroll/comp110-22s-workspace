"""columns  and rows. """

row_data: list[dict[str, str]] = [
    {"name": "UNC", "city": "Chapel Hill"}, 
    {"name": "Duke", "city": "Durham"}
]

col_data: dict[str, list[str]] = {
    "name": ["UNC", "Duke"], 
    "city": ["Chapel Hill", "Durham"]
}

print(col_data["name"])
print(col_data["city"])
print(row_data[0])
print(row_data[1])
print(col_data["city"][1])
print(row_data[1]["city"])
