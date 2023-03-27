from Back_to_the_Bank import textToMoney

def main():
    test_TextToMoney()

def test_TextToMoney():
    assert textToMoney("hello") == 0
    assert textToMoney("HELLO") == 0
    assert textToMoney("hurry up") == 20
    assert textToMoney("Hurry") == 20
    assert textToMoney("do something") == 100
    assert textToMoney("stop") == "stop"
    assert textToMoney("STOP") == "stop"

if __name__ == "__main__":
    main()
