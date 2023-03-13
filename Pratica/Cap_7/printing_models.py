unprinted_designs = ['iphone case', 'robot pendant', 'dode cahedron']
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("\nPrinting " + current_design + "...")

    completed_models.append(current_design)
    print("The following models have been completed:")
    for completed_model in completed_models:
        print("\t" + completed_model)
