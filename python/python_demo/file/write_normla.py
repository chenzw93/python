def write_file(file_path, lines, mode_type="w", encoding_type="utf-8", ):
    with open(file_path, encoding=encoding_type, mode=mode_type) as file_output:
        if lines:
            file_output.writelines("\n".join(lines))
