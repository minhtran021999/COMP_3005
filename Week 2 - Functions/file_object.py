'''
This script shows the file attributes/methods that are available when we
launch a .py file. These attributes/methods allow us to handle txt. 
'''

##### FILE OBJECT METHODS AND ATTRIBUTES #####

with open('helper_script.py', 'r') as f:
    print("=== FILE OBJECT ATTRIBUTES AND METHODS ===")
    print(f"\n\nFile object type: {type(f)}")
    
    # Show all attributes and methods
    
    print("\nAll file object attributes/methods:")
    for item in sorted(dir(f)):
        if not item.startswith('_'):
            attr = getattr(f, item)
            attr_type = "method" if callable(attr) else "attribute"
            print(f"  {item}: {attr_type}")