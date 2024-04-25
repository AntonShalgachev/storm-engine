import os
import xml.etree.ElementTree as ET


msbuild_ns = 'http://schemas.microsoft.com/developer/msbuild/2003'


def main():
    ET.register_namespace('', msbuild_ns)

    for root, _, files in os.walk('.'):
        project_files = [f for f in files if os.path.splitext(f)[1] == '.vcxproj']

        common_prop_sheet_path = os.path.relpath('./CommonPropertySheet.props', root)
        new_element = ET.Element('Import', {'Project': common_prop_sheet_path})

        for f in project_files:
            path = os.path.join(root, f)
            print(path)

            tree = ET.parse(path)
            root = tree.getroot()
            for group in root.findall(".//ns:ImportGroup[@Label='PropertySheets']", namespaces={'ns': msbuild_ns}):
                group.append(new_element)
            
            tree.write(path, xml_declaration=True, encoding='utf-8', method='xml')


if __name__ == '__main__':
    main()