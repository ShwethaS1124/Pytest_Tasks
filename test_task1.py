import pytest


@pytest.fixture(autouse=True)
def setup_and_teardown():
    
    print("\nRunning setup code")

    global age, username, password
    age = 24
    username = "Henry"
    password = "StrongPassword123@"

    yield

    
    print("Running teardown code")


#@pytest.mark.usefixtures("setup_and_teardown")
class TestPasswordChecker:
    #1st Test case
    @pytest.mark.dependency(name="age_check")
    def test_agevalidation(self):
        assert age >= 18, "User age is below 18"


    #2nd Test case
    @pytest.mark.dependency(depends=["age_check"])
    def test_username_password(self):
        assert username != ""
        assert password != ""


    #3rd Test case
    @pytest.mark.dependency(depends=["age_check"])
    def test_password_length(self):
        assert len(password) >= 15


    #4th Test case
    @pytest.mark.dependency(depends=["age_check"])
    def test_casevalidate(self):

        upper = any(c.isupper() for c in password)
        lower = any(c.islower() for c in password)

        assert upper and lower


    #5th Test case
    @pytest.mark.dependency(depends=["age_check"])
    def test_numericcharacter(self):

        digit = any(c.isdigit() for c in password)

        assert digit


    #6th Test case
    @pytest.mark.dependency(depends=["age_check"])
    def test_usernamenotinpassword(self):

        assert username.lower() not in password.lower()


    #7th Test case
    @pytest.mark.dependency(depends=["age_check"])

    def test_special_character(self):

        special_chars = "@#$%"
        assert any(c in special_chars for c in password)