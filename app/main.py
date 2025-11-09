def format_linter_error(error: dict) -> dict:
    my_dict = {
        "line": error.get("line_number", 0),
        "column": error.get("column_number", 0),
        "message": error.get("text", 0),
        "name": error.get("code", 0),
        "source": "flake8",
    }
    return my_dict




def format_single_linter_file(file_path: str, errors: list[dict]) -> dict:
    n_dict = {
        "errors": [format_linter_error(n) for n in errors],
        "path": file_path,
        "status": "passed" if not errors else "failed",
    }
    return n_dict


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(path, errors)
        for path, errors in linter_report.items()
    ]
