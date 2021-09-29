

class AuthValidation():

    auth = False

    def validate(self):
        print ("Validando autorização do Manager ...")
        self.auth = True

    def is_valid(self) -> bool:
        return self.auth

