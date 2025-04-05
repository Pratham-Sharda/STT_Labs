
# file_path = "dependencies_TTS.json"  # Replace with the actual file path
# corrected_file_path = "corrected_file.json"  # New file for corrected content

# # Read the file in binary mode and decode it properly
# with open(file_path, "rb") as f:
#     content = f.read().decode("utf-16")

# # Write the corrected content to a new JSON file
# with open(corrected_file_path, "w", encoding="utf-8") as f:
#     f.write(content)

# print(f"Corrected file saved as: {corrected_file_path}")




# # import json

# # # Load dependency data from JSON file
# # with open("corrected_file.json", "r") as f:
# #     dependencies = json.load(f)

# # # Print a sample of the JSON structure
# # print(json.dumps(dependencies, indent=4))





# import json
# import networkx as nx
# from tqdm import tqdm

# # Load the dependency graph from JSON file
# with open("corrected_file.json", "r") as file:
#     data = json.load(file)

# # Create a directed graph
# G = nx.DiGraph()

# # Populate the graph with nodes and edges from JSON data
# print("Building dependency graph...")
# for module, details in tqdm(data.items(), desc="Processing Modules"):
#     G.add_node(module)  # Add module as node
#     for dep in details.get("imports", []):
#         if dep in data:  # Ensure dependency exists in JSON
#             G.add_edge(module, dep)  # Add directed edge (module → dep)

# # Identify highly coupled modules (high fan-in & fan-out)
# print("Analyzing coupling...")
# coupling_data = {}
# for module in tqdm(G.nodes, desc="Calculating Coupling"):
#     fan_in = len(list(G.predecessors(module)))  # Incoming edges
#     fan_out = len(list(G.successors(module)))   # Outgoing edges
#     coupling_data[module] = {'fan_in': fan_in, 'fan_out': fan_out}

# # Sort by highest total coupling (fan-in + fan-out)
# highly_coupled_modules = sorted(coupling_data.items(), key=lambda x: x[1]['fan_in'] + x[1]['fan_out'], reverse=True)

# # Detect cyclic dependencies
# print("Detecting cyclic dependencies...")
# cycles = list(tqdm(nx.simple_cycles(G), desc="Finding Cycles"))

# # Identify unused (no incoming or outgoing edges) and disconnected modules
# print("Checking for unused and disconnected modules...")
# unused_modules = [node for node in tqdm(G.nodes, desc="Finding Unused Modules") if G.in_degree(node) == 0 and G.out_degree(node) == 0]
# disconnected_modules = list(tqdm(nx.isolates(G), desc="Finding Disconnected Modules"))

# # Assess dependency depth (longest dependency chain)
# print("Calculating dependency depth...")
# try:
#     longest_path = max(nx.all_simple_paths(G, source=min(G.nodes), target=max(G.nodes)), key=len)
#     dependency_depth = len(longest_path)
# except ValueError:
#     dependency_depth = 0  # No valid paths found

# # Print results
# print("\nHighly Coupled Modules (Top 5):")
# for module, details in highly_coupled_modules[:5]:  
#     print(f"{module}: Fan-in = {details['fan_in']}, Fan-out = {details['fan_out']}")

# print("\nCyclic Dependencies Detected:" if cycles else "\nNo Cyclic Dependencies Found.")
# for cycle in cycles:
#     print(" -> ".join(cycle))

# print("\nUnused Modules:", unused_modules)
# print("Disconnected Modules:", disconnected_modules)
# print(f"Dependency Depth: {dependency_depth}")
# print(len(G.nodes), "modules in total")
# print(len(G.edges), "dependencies in total")
# print(len(cycles), "cycles in total")
# print(len(unused_modules), "unused modules in total")
# print(len(disconnected_modules), "disconnected modules in total")
# print("Analysis complete.")


# ##########################

# print("###############################################################################")
# print("###############################################################################")



# import json
# import networkx as nx
# from tqdm import tqdm

# # Load the dependency graph from JSON file
# with open("corrected_file.json", "r") as file:
#     data = json.load(file)

# # Create a directed graph
# G = nx.DiGraph()

# # Populate the graph with nodes and edges from JSON data
# print("Building dependency graph...")
# for module, details in tqdm(data.items(), desc="Processing Modules"):
#     G.add_node(module)  # Add module as node
    
#     # Add dependencies (module → dependencies it imports)
#     for dep in details.get("imports", []):
#         if dep in data:  # Ensure dependency exists in JSON
#             G.add_edge(module, dep)

#     # Add reverse dependencies (module ← modules that import it)
#     for importer in details.get("imported_by", []):
#         if importer in data:  # Ensure dependency exists in JSON
#             G.add_edge(importer, module)

# # Identify highly coupled modules (high fan-in & fan-out)
# print("Analyzing coupling...")
# coupling_data = {}
# for module in tqdm(G.nodes, desc="Calculating Coupling"):
#     fan_in = len(list(G.predecessors(module)))  # Incoming edges
#     fan_out = len(list(G.successors(module)))   # Outgoing edges
#     coupling_data[module] = {'fan_in': fan_in, 'fan_out': fan_out}

# # Sort by highest total coupling (fan-in + fan-out)
# highly_coupled_modules = sorted(coupling_data.items(), key=lambda x: x[1]['fan_in'] + x[1]['fan_out'], reverse=True)

# # Detect cyclic dependencies
# print("Detecting cyclic dependencies...")
# cycles = list(tqdm(nx.simple_cycles(G), desc="Finding Cycles"))

# # Identify unused (no incoming or outgoing edges) and disconnected modules
# print("Checking for unused and disconnected modules...")
# unused_modules = [node for node in tqdm(G.nodes, desc="Finding Unused Modules") if G.in_degree(node) == 0 and G.out_degree(node) == 0]
# disconnected_modules = list(tqdm(nx.isolates(G), desc="Finding Disconnected Modules"))

# # Assess dependency depth (longest dependency chain)
# print("Calculating dependency depth...")
# try:
#     longest_path = max(nx.all_simple_paths(G, source=min(G.nodes), target=max(G.nodes)), key=len)
#     dependency_depth = len(longest_path)
# except ValueError:
#     dependency_depth = 0  # No valid paths found

# # Print results
# print("\nHighly Coupled Modules (Top 5):")
# for module, details in highly_coupled_modules[:5]:  
#     print(f"{module}: Fan-in = {details['fan_in']}, Fan-out = {details['fan_out']}")

# print("\nCyclic Dependencies Detected:" if cycles else "\nNo Cyclic Dependencies Found.")
# for cycle in cycles[-10:]:  # Print first 10 cycles only
#     print(" -> ".join(cycle))

# for cycle in cycles[:10]:  # Print first 10 cycles only
#     print(" -> ".join(cycle))

# for cycle in cycles[-10:]:  # Print first 10 cycles only
#     print((cycle))

# for cycle in cycles[:10]:  # Print first 10 cycles only
#     print((cycle))

# print("\nUnused Modules:", unused_modules if unused_modules else "None")
# print("Disconnected Modules:", disconnected_modules if disconnected_modules else "None")
# print(f"Dependency Depth: {dependency_depth}")

# # Summary
# print(len(G.nodes), "modules in total")
# print(len(G.edges), "dependencies in total")
# print(len(cycles), "cycles in total")
# print(len(unused_modules), "unused modules in total")
# print(len(disconnected_modules), "disconnected modules in total")
# print("Analysis complete.")

# print("###############################################################################")
# print("###############################################################################")


import json
import networkx as nx
from tqdm import tqdm

# Load the dependency graph from JSON file
with open("corrected_file.json", "r") as file:
    data = json.load(file)

# Create a directed graph
G = nx.DiGraph()

# Populate the graph with nodes and edges from JSON data
print("Building dependency graph...")
for module, details in tqdm(data.items(), desc="Processing Modules"):
    G.add_node(module)  # Add module as node
    
    # Add dependencies (module → dependencies it imports)
    for dep in details.get("imports", []):
        if dep in data:  # Ensure dependency exists in JSON
            G.add_edge(module, dep)

    # Add reverse dependencies (module ← modules that import it)
    for importer in details.get("imported_by", []):
        if importer in data:  # Ensure dependency exists in JSON
            G.add_edge(importer, module)

# Identify fan-in and fan-out for each module
print("Analyzing coupling...")
coupling_data = {}
for module in tqdm(G.nodes, desc="Calculating Coupling"):
    fan_in = len(list(G.predecessors(module)))  # Incoming edges (number of modules that depend on this module)
    fan_out = len(list(G.successors(module)))   # Outgoing edges (number of modules this module depends on)
    coupling_data[module] = {'fan_in': fan_in, 'fan_out': fan_out}

# Detect cyclic dependencies
print("Detecting cyclic dependencies...")
cycles = list(tqdm(nx.simple_cycles(G), desc="Finding Cycles"))

# Identify unused (no incoming or outgoing edges) and disconnected modules
print("Checking for unused and disconnected modules...")
unused_modules = [node for node in tqdm(G.nodes, desc="Finding Unused Modules") if G.in_degree(node) == 0 and G.out_degree(node) == 0]
disconnected_modules = list(tqdm(nx.isolates(G), desc="Finding Disconnected Modules"))

# Identify modules that import files but are not imported by any other module
print("Finding modules that import others but are not imported themselves...")
import_only_modules = [node for node in G.nodes if G.in_degree(node) == 0 and G.out_degree(node) > 0]

# Assess dependency depth (longest dependency chain)
print("Calculating dependency depth...")
try:
    longest_path = max(nx.all_simple_paths(G, source=min(G.nodes), target=max(G.nodes)), key=len)
    dependency_depth = len(longest_path)
except ValueError:
    dependency_depth = 0  # No valid paths found

# Print results
print("\nHighly Coupled Modules (Top 5 by Total Dependencies):")
highly_coupled_modules = sorted(coupling_data.items(), key=lambda x: x[1]['fan_in'] + x[1]['fan_out'], reverse=True)[:5]
for module, details in highly_coupled_modules:
    print(f"{module}: Fan-in = {details['fan_in']}, Fan-out = {details['fan_out']}")

print("\nCyclic Dependencies Detected:" if cycles else "\nNo Cyclic Dependencies Found.")
for cycle in cycles[:10]:  # Print first 10 cycles only
    print(" -> ".join(cycle))

print("\nUnused Modules:", unused_modules if unused_modules else "None")
print("Disconnected Modules:", disconnected_modules if disconnected_modules else "None")
print(f"Dependency Depth: {dependency_depth}")

# Print modules that only import but are not imported
print("\nModules that import others but are not imported by any:")
print(import_only_modules if import_only_modules else "None")

# Summary
print(len(G.nodes), "modules in total")
print(len(G.edges), "dependencies in total")
print(len(cycles), "cycles in total")
print(len(unused_modules), "unused modules in total")
print(len(disconnected_modules), "disconnected modules in total")
print(len(import_only_modules), "modules that only import but are not imported in total")
print("Analysis complete.")
print("###############################################################################")

# Determine Top 5 Core Modules (High Fan-in & Low Fan-out)
print("\nTop 5 Core Modules (High Fan-in & Low Fan-out):")
core_modules = sorted(coupling_data.items(), key=lambda x: (x[1]['fan_in'], -x[1]['fan_out']), reverse=True)[:5]
for module, details in core_modules:
    print(f"{module}: Fan-in = {details['fan_in']}, Fan-out = {details['fan_out']}")

# Dependency impact assessment for core modules
print("\nDependency Impact Assessment:")
for core_module, _ in core_modules:
    affected_modules = list(nx.descendants(G, core_module))
    print(f"Changes in {core_module} would affect: {affected_modules if affected_modules else 'None'}")

# Identify Modules at Risk of Breaking the System (High Fan-out)
print("\nModules at Risk of Breaking the System (High Fan-out):")
at_risk_modules = sorted(coupling_data.items(), key=lambda x: x[1]['fan_out'], reverse=True)[:5]
for module, details in at_risk_modules:
    print(f"{module}: Fan-in = {details['fan_in']}, Fan-out = {details['fan_out']}")


# import json
# import networkx as nx
# from tqdm import tqdm

# # Load the dependency graph from JSON file
# with open("corrected_file.json", "r") as file:
#     data = json.load(file)

# # Create a directed graph
# G = nx.DiGraph()

# # Populate the graph with nodes and edges from JSON data
# print("Building dependency graph...")
# for module, details in tqdm(data.items(), desc="Processing Modules"):
#     G.add_node(module)  # Add module as node
    
#     # Add dependencies (module → dependencies it imports)
#     for dep in details.get("imports", []):
#         if dep in data:  # Ensure dependency exists in JSON
#             G.add_edge(module, dep)

#     # Add reverse dependencies (module ← modules that import it)
#     for importer in details.get("imported_by", []):
#         if importer in data:  # Ensure dependency exists in JSON
#             G.add_edge(importer, module)

# # Identify highly coupled modules (high fan-in & fan-out)
# print("Analyzing coupling...")
# coupling_data = {}
# for module in tqdm(G.nodes, desc="Calculating Coupling"):
#     fan_in = len(list(G.predecessors(module)))  # Incoming edges
#     fan_out = len(list(G.successors(module)))   # Outgoing edges
#     coupling_data[module] = {'fan_in': fan_in, 'fan_out': fan_out}

# # Sort by highest total coupling (fan-in + fan-out)
# highly_coupled_modules = sorted(coupling_data.items(), key=lambda x: x[1]['fan_in'] + x[1]['fan_out'], reverse=True)

# # Detect cyclic dependencies
# print("Detecting cyclic dependencies...")
# cycles = list(tqdm(nx.simple_cycles(G), desc="Finding Cycles"))

# # Identify unused (no incoming or outgoing edges) and disconnected modules
# print("Checking for unused and disconnected modules...")
# unused_modules = [node for node in tqdm(G.nodes, desc="Finding Unused Modules") if G.in_degree(node) == 0 and G.out_degree(node) == 0]
# disconnected_modules = list(tqdm(nx.isolates(G), desc="Finding Disconnected Modules"))

# # Identify modules that import files but are not imported by any other module
# print("Finding modules that import others but are not imported themselves...")
# import_only_modules = [node for node in G.nodes if G.in_degree(node) == 0 and G.out_degree(node) > 0]

# # Assess dependency depth (longest dependency chain)
# print("Calculating dependency depth...")
# try:
#     longest_path = max(nx.all_simple_paths(G, source=min(G.nodes), target=max(G.nodes)), key=len)
#     dependency_depth = len(longest_path)
# except ValueError:
#     dependency_depth = 0  # No valid paths found

# # Print results
# print("\nHighly Coupled Modules (Top 5):")
# for module, details in highly_coupled_modules[:5]:  
#     print(f"{module}: Fan-in = {details['fan_in']}, Fan-out = {details['fan_out']}")

# print("\nCyclic Dependencies Detected:" if cycles else "\nNo Cyclic Dependencies Found.")
# for cycle in cycles[:10]:  # Print first 10 cycles only
#     print(" -> ".join(cycle))

# print("\nUnused Modules:", unused_modules if unused_modules else "None")
# print("Disconnected Modules:", disconnected_modules if disconnected_modules else "None")
# print(f"Dependency Depth: {dependency_depth}")

# # Print modules that only import but are not imported
# print("\nModules that import others but are not imported by any:")
# print(import_only_modules if import_only_modules else "None")

# # Summary
# print(len(G.nodes), "modules in total")
# print(len(G.edges), "dependencies in total")
# print(len(cycles), "cycles in total")
# print(len(unused_modules), "unused modules in total")
# print(len(disconnected_modules), "disconnected modules in total")
# print(len(import_only_modules), "modules that only import but are not imported in total")
# print("Analysis complete.")
# print("###############################################################################")

# import json
# import networkx as nx
# from tqdm import tqdm

# # Load the dependency graph from JSON file
# with open("corrected_file.json", "r") as file:
#     data = json.load(file)

# # Create a directed graph
# G = nx.DiGraph()

# # Populate the graph with nodes and edges from JSON data
# print("Building dependency graph...")
# for module, details in tqdm(data.items(), desc="Processing Modules"):
#     G.add_node(module)  # Add module as node
    
#     # Add dependencies (module → dependencies it imports)
#     for dep in details.get("imports", []):
#         if dep in data:  # Ensure dependency exists in JSON
#             G.add_edge(module, dep)

#     # Add reverse dependencies (module ← modules that import it)
#     for importer in details.get("imported_by", []):
#         if importer in data:  # Ensure dependency exists in JSON
#             G.add_edge(importer, module)

# # Identify highly coupled modules (high fan-in & fan-out)
# print("Analyzing coupling...")
# coupling_data = {}
# for module in tqdm(G.nodes, desc="Calculating Coupling"):
#     fan_in = len(list(G.predecessors(module)))  # Incoming edges
#     fan_out = len(list(G.successors(module)))   # Outgoing edges
#     coupling_data[module] = {'fan_in': fan_in, 'fan_out': fan_out}

# # Sort by highest total coupling (fan-in + fan-out)
# highly_coupled_modules = sorted(coupling_data.items(), key=lambda x: x[1]['fan_in'] + x[1]['fan_out'], reverse=True)

# # Detect cyclic dependencies
# print("Detecting cyclic dependencies...")
# cycles = list(tqdm(nx.simple_cycles(G), desc="Finding Cycles"))

# # Identify different types of modules based on their connectivity
# print("Analyzing module connectivity patterns...")

# # Unused modules (no incoming or outgoing edges)
# unused_modules = [node for node in tqdm(G.nodes, desc="Finding Unused Modules") 
#                 if G.in_degree(node) == 0 and G.out_degree(node) == 0]

# # Entry points (__main__-like): modules that import others but aren't imported themselves
# entry_point_modules = [node for node in tqdm(G.nodes, desc="Finding Entry Point Modules") 
#                      if G.in_degree(node) == 0 and G.out_degree(node) > 0]

# # Sort entry points by how many modules they import (descending)
# entry_point_details = [(module, G.out_degree(module)) for module in entry_point_modules]
# entry_point_details.sort(key=lambda x: x[1], reverse=True)

# # Leaf modules: modules that are imported but don't import others
# leaf_modules = [node for node in tqdm(G.nodes, desc="Finding Leaf Modules")
#                if G.out_degree(node) == 0 and G.in_degree(node) > 0]

# # Intermediate modules: modules that both import and are imported
# intermediate_modules = [node for node in tqdm(G.nodes, desc="Finding Intermediate Modules")
#                       if G.out_degree(node) > 0 and G.in_degree(node) > 0]

# # Calculate actual dependency depth
# print("Calculating dependency depth...")
# dependency_depths = {}
# connected_components = list(nx.weakly_connected_components(G))
# for i, component in enumerate(connected_components):
#     subgraph = G.subgraph(component)
    
#     # Find the longest simple path in this component
#     max_path_length = 0
#     for source in tqdm(subgraph.nodes, desc=f"Component {i+1}/{len(connected_components)}", leave=False):
#         for target in subgraph.nodes:
#             if source != target:
#                 try:
#                     # Find all simple paths between source and target
#                     paths = list(nx.all_simple_paths(subgraph, source, target))
#                     if paths:
#                         longest_path = max(paths, key=len)
#                         max_path_length = max(max_path_length, len(longest_path))
#                 except (nx.NetworkXNoPath, ValueError):
#                     continue
    
#     dependency_depths[f"Component {i+1}"] = max_path_length

# # Dependency Impact Assessment
# print("Performing dependency impact assessment...")

# # 1. Impact of changes in core modules
# # Identify core modules (those with highest combination of fan-in and fan-out)
# core_modules = [module for module, _ in highly_coupled_modules[:5]]

# # For each core module, calculate its impact factor 
# # (how many modules would be affected if it changes)
# impact_assessment = {}
# for module in tqdm(core_modules, desc="Assessing Core Module Impact"):
#     # Find all descendants (modules that depend on this module)
#     descendants = list(nx.descendants(G, module))
#     impact_assessment[module] = {
#         'affected_modules_count': len(descendants),
#         'affected_modules': descendants,
#         'impact_percentage': len(descendants) / len(G.nodes) * 100 if G.nodes else 0
#     }

# # 2. Identify risky modules (high fan-in and involved in cycles)
# # Modules with many dependents are risky to modify
# risky_modules = {}
# cycle_modules = set()
# for cycle in cycles:
#     cycle_modules.update(cycle)

# for module in tqdm(G.nodes, desc="Identifying Risky Modules"):
#     fan_in = coupling_data[module]['fan_in']
#     in_cycle = module in cycle_modules
    
#     # Risk factor: combination of fan-in and cycle involvement
#     risk_score = fan_in * (2 if in_cycle else 1)
    
#     if risk_score > 0:  # Only include modules with some risk
#         risky_modules[module] = {
#             'risk_score': risk_score,
#             'fan_in': fan_in,
#             'in_cycle': in_cycle,
#             'dependents': list(G.predecessors(module))
#         }

# # Sort risky modules by risk score
# risky_modules_sorted = sorted(risky_modules.items(), key=lambda x: x[1]['risk_score'], reverse=True)

# # Print results
# print("\nHighly Coupled Modules (Top 5):")
# for module, details in highly_coupled_modules[:5]:  
#     print(f"{module}: Fan-in = {details['fan_in']}, Fan-out = {details['fan_out']}")

# print("\nCyclic Dependencies Detected:" if cycles else "\nNo Cyclic Dependencies Found.")
# for i, cycle in enumerate(cycles[:10]):  # Print first 10 cycles only
#     print(f"Cycle {i+1}: {' -> '.join(cycle)}")

# # Print entry point modules (likely __main__-like modules)
# print("\nEntry Point Modules (importing others but not imported):")
# if entry_point_details:
#     for module, out_degree in entry_point_details[:10]:  # Show top 10
#         print(f"{module}: imports {out_degree} other modules")
#     if len(entry_point_details) > 10:
#         print(f"...and {len(entry_point_details) - 10} more")
# else:
#     print("None found")

# # Print module type statistics
# print("\nModule Type Distribution:")
# print(f"Entry point modules: {len(entry_point_modules)}")
# print(f"Leaf modules: {len(leaf_modules)}")
# print(f"Intermediate modules: {len(intermediate_modules)}")
# print(f"Unused modules: {len(unused_modules)}")

# print("\nDependency Depth by Component:")
# for component, depth in dependency_depths.items():
#     print(f"{component}: {depth} levels")

# # Print impact assessment
# print("\nCore Module Impact Assessment:")
# for module, impact in impact_assessment.items():
#     print(f"{module}: Would affect {impact['affected_modules_count']} modules ({impact['impact_percentage']:.2f}% of system)")

# print("\nRisky Modules (Top 5):")
# for module, details in risky_modules_sorted[:5]:
#     print(f"{module}: Risk Score = {details['risk_score']}, Fan-in = {details['fan_in']}, In Cycle = {details['in_cycle']}")

# # Summary
# print("\nSummary:")
# print(len(G.nodes), "modules in total")
# print(len(G.edges), "dependencies in total")
# print(len(cycles), "cycles in total")
# print(len(unused_modules), "unused modules in total")
# print(len(entry_point_modules), "entry point modules in total")
# print("Analysis complete.")