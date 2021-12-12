from gendiff.scripts.gendiff import generated_diff


def test_generated_diff():

    with open("fixtures/result_json.txt", "r") as file_result:
        content = file_result.read()
        assert generated_diff('fixtures/file1.json',
                              'fixtures/file2.json') == content
