class TestSuite:

    def test_case_1(self, case_data):
        time = int(case_data)
        print(f'    > Received from fixture timestamp is: {time}')
        assert time % 2 == 0
