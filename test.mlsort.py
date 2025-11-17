import subprocess

def run(input_data):
    p = subprocess.Popen(
        ["python3", "mlsort"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True
    )
    out, _ = p.communicate(input_data)
    return out.strip().split("\n")

def test_int_sort():
    assert run("3\n1\n2\n") == ["1", "2", "3"]

def test_float_sort():
    assert run("3.1\n2.0\n10.5\n") == ["2.0", "3.1", "10.5"]

def test_date_sort():
    assert run("2024-01-01\n2023-12-10\n") == ["2023-12-10", "2024-01-01"]

def test_text_sort():
    assert run("banana\napple\ncarrot\n") == ["apple", "banana", "carrot"]
