import os

try:
    import sass
except ImportError:
    print("You need to install the 'libsass' module, check the readme for more info.")
    exit(1)

FILE_ALL_IN = "./scss/main-all.scss"
FILE_MAIN_IN = "./scss/main-base.scss"
FILE_CODE_IN = "./scss/main-code.scss"
FILE_GRID_IN = "./scss/main-grid.scss"
FILE_FANCY_IN = "./scss/main-fancy.scss"

FILE_ALL_OUT = "./css/simplette.all.min.css"
FILE_MAIN_OUT = "./css/simplette.base.min.css"
FILE_CODE_OUT = "./css/simplette.code.min.css"
FILE_GRID_OUT = "./css/simplette.grid.min.css"
FILE_FANCY_OUT = "./css/simplette.fancy.min.css"


def compile_file(input_path, output_path):
    if os.path.exists(output_path):
        os.remove(output_path)
    
    try:
        css = sass.compile(
            filename=input_path,
            output_style="compressed",
            include_paths=["./scss/"]
        )
    except sass.CompileError as err:
        print("Failed to compile {} !".format(input_path))
        print(err)
        exit(2)
    
    css_file = open(output_path, "wb")
    css_file.write(css.encode("utf-8"))
    css_file.close()


print("Compiling...")
compile_file(FILE_ALL_IN, FILE_ALL_OUT)
compile_file(FILE_MAIN_IN, FILE_MAIN_OUT)
compile_file(FILE_CODE_IN, FILE_CODE_OUT)
compile_file(FILE_GRID_IN, FILE_GRID_OUT)
compile_file(FILE_FANCY_IN, FILE_FANCY_OUT)
print("Done !")
