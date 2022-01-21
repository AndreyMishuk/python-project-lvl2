from gendiff.scripts.gendiff import generated_diff


def test_generated_diff():

    result_str = ''

    diff_str_json = generated_diff('./tests/fixtures/file1.json',
                                   './tests/fixtures/file2.json')

    diff_str_yaml = generated_diff('./tests/fixtures/file1.yml',
                                   './tests/fixtures/file2.yaml')

    with (open("./tests/fixtures/result_str_generated_diff.txt", "r")
          as file_result):
        result_str = file_result.read()

    assert diff_str_json == result_str.strip()
    assert diff_str_yaml == result_str.strip()
