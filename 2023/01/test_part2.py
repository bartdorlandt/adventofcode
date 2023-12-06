import day01_part2 as p2


def test_first_and_last():
    assert 12 == p2.first_and_last("one692")
    assert 67 == p2.first_and_last("tbsxkhhv6twozrtczg6seven")
    assert 89 == p2.first_and_last("ccpeightbcvknglvcv81gcjnlnfnine9")
    assert 42 == p2.first_and_last("4twoscpht")
    assert 94 == p2.first_and_last("qdgdrtx9onefourdcvctldjnpcdjbc")
    assert 48 == p2.first_and_last("cjxkxsgmql4xxgjtpdcbmsixeight")
    assert 79 == p2.first_and_last("739")
    assert 61 == p2.first_and_last("sixsixgnpprvjdkgvqmr1")
    assert 26 == p2.first_and_last("twothree6vpnvvnshn")
    assert 87 == p2.first_and_last("eightone7threenl7mtxbmkpkzqzljrdk")
    assert 29 == p2.first_and_last("dtwoneeight6llzcxssgrdfjmjvfbvtwo9")
    assert 85 == p2.first_and_last("feightwo5")
    assert 14 == p2.first_and_last("rloneight124")
    assert 68 == p2.first_and_last("csgjjk6xbq4mnhmsix3nlstqqfpxtvfoneightvk")
    assert 18 == p2.first_and_last("crvhlfone7xsqhkshpsix2nine73oneighttq")
    assert 83 == p2.first_and_last("8xplcnjxfthreeeightthree")
