import os, json, pathlib
out = os.environ.get("OUTPUT_DIR", "/tmp/output")
pathlib.Path(out).mkdir(parents=True, exist_ok=True)
with open(os.path.join(out, "hello.txt"), "w") as f:
    f.write("hello from python\n")
print("done")
