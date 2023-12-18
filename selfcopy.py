import shutil

def duplicate_script():
    with open(__file__, 'r') as current_file:
        script_contents = current_file.read()

    print(script_contents)
    
    # with open(new_file_name, 'w') as new_file:
    #     new_file.write(script_contents)

    # print(f"Script duplicated as {new_file_name}")

if __name__ == "__main__":
    duplicate_script()
