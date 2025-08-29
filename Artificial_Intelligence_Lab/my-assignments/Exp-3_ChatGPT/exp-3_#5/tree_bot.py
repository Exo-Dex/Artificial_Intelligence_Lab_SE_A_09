###Prompt:
"""
can we build a basic bot which will detect the required data just by the tree's common names and scientific name
"""

# Simple Tree Info Bot
trees = {
    "Neem": {"scientific": "Azadirachta indica", "uses": "Medicinal, shade, pesticide"},
    "Mango": {"scientific": "Mangifera indica", "uses": "Fruit, timber, shade"},
    "Peepal": {"scientific": "Ficus religiosa", "uses": "Sacred, oxygen, shade"}
}

def get_tree_info(query):
    # Search by common name
    if query in trees:
        return f"Common: {query}, Scientific: {trees[query]['scientific']}, Uses: {trees[query]['uses']}"
    
    # Search by scientific name
    for common, info in trees.items():
        if query.lower() == info["scientific"].lower():
			return f"Common: {common}, Scientific: {info['scientific']}, Uses: {info['uses']}"
    
	return "Tree not found in database."

# Example
print(get_tree_info("Neem"))
print(get_tree_info("Azadirachta indica"))


###Output:
"""
Common: Neem, Scientific: Azadirachta indica, Uses: Medicinal, shade, pesticide
Common: Neem, Scientific: Azadirachta indica, Uses: Medicinal, shade, pesticide
"""
