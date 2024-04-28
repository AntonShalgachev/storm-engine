import os
import xml.etree.ElementTree as ET


msbuild_ns = 'http://schemas.microsoft.com/developer/msbuild/2003'


def add_common_property_sheet(root, filename):
    path = os.path.join(root, filename)
    print(path)

    common_prop_sheet_path = os.path.relpath('./CommonPropertySheet.props', root)
    new_element = ET.Element('Import', {'Project': common_prop_sheet_path})

    tree = ET.parse(path)
    root = tree.getroot()
    for group in root.findall(".//ns:ImportGroup[@Label='PropertySheets']", namespaces={'ns': msbuild_ns}):
        group.append(new_element)
    
    tree.write(path, xml_declaration=True, encoding='utf-8', method='xml')


def add_storm_engine_module_property_sheet(root, filename):
    path = os.path.join(root, filename)
    print(path)

    common_prop_sheet_path = os.path.relpath('./StormEngineModule.props', root)
    new_element = ET.Element('Import', {'Project': common_prop_sheet_path})

    tree = ET.parse(path)
    root = tree.getroot()
    for group in root.findall(".//ns:PropertyGroup[@Label='Configuration']", namespaces={'ns': msbuild_ns}):
        type_element = group.find('ns:ConfigurationType', namespaces={'ns': msbuild_ns})
        assert(type_element is not None)
        type = type_element.text
        assert type == 'DynamicLibrary' or type == 'Application'
        if type != 'DynamicLibrary':
            return
        
    for group in root.findall(".//ns:ImportGroup[@Label='PropertySheets']", namespaces={'ns': msbuild_ns}):
        group.append(new_element)
    
    tree.write(path, xml_declaration=True, encoding='utf-8', method='xml')


def unify_output_paths(root, filename):
    path = os.path.join(root, filename)
    print(path)

    tree = ET.parse(path)
    parent_map = {c: p for p in tree.iter() for c in p}
    root = tree.getroot()
    for node in root.findall(".//ns:PropertyGroup/ns:OutDir", namespaces={'ns': msbuild_ns}):
        parent_map[node].remove(node)
    for node in root.findall(".//ns:PropertyGroup/ns:IntDir", namespaces={'ns': msbuild_ns}):
        parent_map[node].remove(node)
    for node in root.findall(".//ns:Link/ns:OutputFile", namespaces={'ns': msbuild_ns}):
        parent_map[node].remove(node)
    for node in root.findall(".//ns:ItemDefinitionGroup/ns:ClCompile/ns:AssemblerListingLocation", namespaces={'ns': msbuild_ns}):
        parent_map[node].remove(node)
    for node in root.findall(".//ns:ItemDefinitionGroup/ns:ClCompile/ns:ObjectFileName", namespaces={'ns': msbuild_ns}):
        parent_map[node].remove(node)
    for node in root.findall(".//ns:ItemDefinitionGroup/ns:ClCompile/ns:ProgramDataBaseFileName", namespaces={'ns': msbuild_ns}):
        parent_map[node].remove(node)
    for node in root.findall(".//ns:ItemDefinitionGroup/ns:Link/ns:ProgramDatabaseFile", namespaces={'ns': msbuild_ns}):
        parent_map[node].remove(node)
    for node in root.findall(".//ns:ItemDefinitionGroup/ns:Link/ns:ImportLibrary", namespaces={'ns': msbuild_ns}):
        parent_map[node].remove(node)
    for node in root.findall(".//ns:PropertyGroup/ns:LinkIncremental", namespaces={'ns': msbuild_ns}):
        parent_map[node].remove(node)
    for node in root.findall(".//ns:ItemDefinitionGroup/ns:ClCompile/ns:MinimalRebuild", namespaces={'ns': msbuild_ns}):
        parent_map[node].remove(node)
    for node in root.findall(".//ns:ItemDefinitionGroup/ns:ClCompile/ns:PrecompiledHeaderOutputFile", namespaces={'ns': msbuild_ns}):
        parent_map[node].remove(node)
    for node in root.findall(".//ns:ItemDefinitionGroup/ns:Midl", namespaces={'ns': msbuild_ns}):
        parent_map[node].remove(node)
    
    tree.write(path, xml_declaration=True, encoding='utf-8', method='xml')


def main():
    ET.register_namespace('', msbuild_ns)

    for root, _, files in os.walk('.'):
        project_files = [f for f in files if os.path.splitext(f)[1] == '.vcxproj']

        for f in project_files:
            # add_common_property_sheet(root, f)
            # add_storm_engine_module_property_sheet(root, f)
            unify_output_paths(root, f)
            pass


if __name__ == '__main__':
    main()