import os

NODE_CATEGORY = "path-util"


class PathAbspath:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"path": ("STRING", {"default": ""})}}

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("abspath",)
    FUNCTION = "run"
    CATEGORY = NODE_CATEGORY

    def run(self, path):
        abspath = os.path.abspath(path)
        return (abspath,)


class PathRelpath:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"path": ("STRING", {"default": ""})}}

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("relpath",)
    FUNCTION = "run"
    CATEGORY = NODE_CATEGORY

    def run(self, path):
        relpath = os.path.relpath(path)
        return (relpath,)


class PathBasename:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "path": ("STRING", {"default": ""}),
                "without_ext": ("BOOLEAN", {"default": False}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("basename",)
    FUNCTION = "run"
    CATEGORY = NODE_CATEGORY

    def run(self, path, without_ext):
        basename = os.path.basename(path)
        if without_ext:
            return (os.path.splitext(basename)[0],)
        else:
            return (basename,)


class PathDirname:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"path": ("STRING", {"default": ""})}}

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("dirname",)
    FUNCTION = "run"
    CATEGORY = NODE_CATEGORY

    def run(self, path):
        dirname = os.path.dirname(path)
        return (dirname,)


class PathSplitext:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"path": ("STRING", {"default": ""})}}

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("root", "ext")
    FUNCTION = "run"
    CATEGORY = NODE_CATEGORY

    def run(self, path):
        root, ext = os.path.splitext(path)
        return (root, ext)


class PathJoin:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "string1": ("STRING", {"default": ""}),
                "string2": ("STRING", {"default": ""}),
            },
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("root", "ext")
    FUNCTION = "run"
    CATEGORY = NODE_CATEGORY

    def run(self, string1, string2):
        path = os.path.join(string1, string2)
        return (path,)


class PathExists:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {"path": ("STRING", {"default": ""})},
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("exist",)
    FUNCTION = "run"
    CATEGORY = NODE_CATEGORY

    def run(self, path):
        exist = os.path.exists(path)
        return (exist,)


class PathIsfile:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {"path": ("STRING", {"default": ""})},
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("isfile",)
    FUNCTION = "run"
    CATEGORY = NODE_CATEGORY

    def run(self, path):
        isfile = os.path.isfile(path)
        return (isfile,)


class PathIsdir:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {"path": ("STRING", {"default": ""})},
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("isdir",)
    FUNCTION = "run"
    CATEGORY = NODE_CATEGORY

    def run(self, path):
        isdir = os.path.isdir(path)
        return (isdir,)


NODE_CLASS_MAPPINGS = {
    "path_util_PathAbspath": PathAbspath,
    "path_util_PathRelpath": PathRelpath,
    "path_util_PathBasename": PathBasename,
    "path_util_PathDirname": PathDirname,
    "path_util_PathSplitext": PathSplitext,
    "path_util_PathJoin": PathJoin,
    "path_util_PathExists": PathExists,
    "path_util_PathIsfile": PathIsfile,
    "path_util_PathIsdir": PathIsdir,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "path_util_PathAbspath": "Path Abspath",
    "path_util_PathRelpath": "Path Relpath",
    "path_util_PathBasename": "Path Basename",
    "path_util_PathDirname": "Path Dirname",
    "path_util_PathSplitext": "Path Splitext",
    "path_util_PathJoin": "Path Join",
    "path_util_PathExists": "Path Exists",
    "path_util_PathIsfile": "Path Isfile",
    "path_util_PathIsdir": "Path Isdir",
}
