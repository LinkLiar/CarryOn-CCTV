import os
import importlib.machinery
import importlib.util


def path_import(file):
    loader_details = (
        importlib.machinery.ExtensionFileLoader,
        importlib.machinery.EXTENSION_SUFFIXES
    )
    tools_finder = importlib.machinery.FileFinder(
        os.path.dirname(file), loader_details)
    print("FileFinder: ", tools_finder)
    toolbox_specs = tools_finder.find_spec(
        os.path.basename(file).split(".")[0])
    print("find_spec: ", toolbox_specs)
    toolbox = importlib.util.module_from_spec(toolbox_specs)
    print("module: ", toolbox)
    toolbox_specs.loader.exec_module(toolbox)
    print("导入成功 path_import(): ", toolbox)
    print("检查sys中是否包含了此模块: ", toolbox in sys.modules)
    print("******************* 动态加载模块完成 *************************\n")
    return toolbox
