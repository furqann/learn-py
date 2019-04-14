import utils  # It's one of using module but you have to write the module name ever you call its function.
from utils import find_max  # other calling module but now you are calling only the required method

print(utils.find_max([25,30,100,1000,9]))

print(find_max([500,85,99,6,9]))
